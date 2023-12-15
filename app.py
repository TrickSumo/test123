import requests
import json
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello World"
