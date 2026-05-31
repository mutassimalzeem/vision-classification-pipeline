from pathlib import Path
from fastapi import FastAPI, UploadFile, File, HTTPException
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np
import io

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "digit_model.h5"
model = keras.models.load_model(MODEL_PATH)


def preprocess_digit_image(image_bytes: bytes) -> np.ndarray:
    image = Image.open(io.BytesIO(image_bytes))
    image = ImageOps.exif_transpose(image)

    if image.mode in ("RGBA", "LA"):
        background = Image.new("RGBA", image.size, (255, 255, 255, 255))
        background.alpha_composite(image.convert("RGBA"))
        image = background.convert("L")
    else:
        image = image.convert("L")

    pixels = np.asarray(image, dtype=np.uint8)
    if np.median(pixels) > 127:
        pixels = 255 - pixels

    threshold = max(20, int(pixels.max() * 0.2))
    foreground_mask = pixels > threshold
    border_margin = max(2, int(round(min(pixels.shape) * 0.01)))
    foreground_mask[:border_margin, :] = False
    foreground_mask[-border_margin:, :] = False
    foreground_mask[:, :border_margin] = False
    foreground_mask[:, -border_margin:] = False

    foreground = np.argwhere(foreground_mask)
    if foreground.size == 0:
        raise ValueError("Image does not contain a visible digit.")

    y_min, x_min = foreground.min(axis=0)
    y_max, x_max = foreground.max(axis=0) + 1
    digit_pixels = (foreground_mask[y_min:y_max, x_min:x_max] * 255).astype(np.uint8)
    digit = Image.fromarray(digit_pixels)

    width, height = digit.size
    scale = 20.0 / max(width, height)
    resized_size = (
        max(1, int(round(width * scale))),
        max(1, int(round(height * scale))),
    )
    digit = digit.resize(resized_size, Image.Resampling.LANCZOS)

    canvas = Image.new("L", (28, 28), 0)
    offset = ((28 - resized_size[0]) // 2, (28 - resized_size[1]) // 2)
    canvas.paste(digit, offset)

    img_array = np.asarray(canvas, dtype=np.float32) / 255.0
    return img_array.reshape(1, 28, 28, 1)

@app.get("/")
async def root():
    return {"message": "Digit classifier API is running"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()

    try:
        input_data = preprocess_digit_image(image_bytes)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    prediction = model.predict(input_data)
    predicted_digit = int(np.argmax(prediction[0]))
    confidence = float(np.max(prediction[0]))
    probabilities = {
        str(index): float(probability)
        for index, probability in enumerate(prediction[0])
    }

    return {
        "filename": file.filename,
        "predicted_digit": predicted_digit,
        "confidence": confidence,
        "probabilities": probabilities,
    }
