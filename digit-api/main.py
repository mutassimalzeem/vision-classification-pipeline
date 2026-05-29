from pathlib import Path
import io

import numpy as np
from fastapi import FastAPI, File, UploadFile
from PIL import Image
from tensorflow import keras


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "digit_model.h5"
model = keras.models.load_model(MODEL_PATH)


@app.get("/")
async def root():
    return {"message": "Digit classifier API is running"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()

    image = Image.open(io.BytesIO(image_bytes)).convert("L")
    image = image.resize((28, 28))

    img_array = np.array(image, dtype=np.float32) / 255.0
    input_data = img_array.reshape(1, 28, 28, 1)

    prediction = model.predict(input_data)
    predicted_digit = int(np.argmax(prediction[0]))
    confidence = float(np.max(prediction[0]))

    return {
        "filename": file.filename,
        "predicted_digit": predicted_digit,
        "confidence": confidence,
    }
