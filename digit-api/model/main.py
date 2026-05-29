from fastapi import FastAPI, UploadFile, File
import joblib, io
from pydantic import BaseModel
import numpy as np
from PIL import Image


model = joblib.load('digit-api\\model\\digit_model.h5')
app = FastAPI()



@app.get('/')
async def root():
    return {"message": 'Hello World'}

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
    input_img = await file.read()
    image = Image.open 
    prediction = model.predict(input_data)