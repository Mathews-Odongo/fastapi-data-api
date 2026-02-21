from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load dataset
data = pd.read_csv("data.csv")

@app.get("/")
def home():
    return {"message": "Welcome to the Data API!"}

@app.get("/summary")
def summary():
    column = data.select_dtypes(include='number').columns[0]
    return {
        "mean": float(data[column].mean()),
        "min": float(data[column].min()),
        "max": float(data[column].max())
    }

@app.get("/count")
def count():
    return {"rows": len(data)}
