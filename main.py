from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import pandas as pd
import os

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks.csv file into memory
df = pd.read_csv("marks.csv")

@app.get("/api")
def get_marks(name: List[str] = []):
    result = []
    for n in name:
        row = df[df["name"] == n]
        if not row.empty:
            result.append(int(row.iloc[0]["marks"]))
        else:
            result.append(None)
    return {"marks": result}
