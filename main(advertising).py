
# creating the FastApi() for the model 
# we use it to convert the model into api
from matplotlib.pyplot import cla
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

joblib.load("linemodel.pkl")

class datascience(BaseModel):
    StudyHours:float

#api end point
@app.get("/")
def test():
    return {"msg":"uvicorn is running"}

