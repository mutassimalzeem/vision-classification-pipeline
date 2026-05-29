from fastapi import FastAPI, UploadFile, File
import joblib, io
from pydantic import BaseModel
import numpy as np


model = joblib.load('digit-api\\model\\digit_model.h5')
app = FastAPI()


class ModelInput(BaseModel):
    pass

@app.get('/')
async def root():
    return {"message": 'Hello World'}

@app.post('/predict')
async def predict(data: ModelInput):
    input_df = 
    prediction = model.predict(input_df)