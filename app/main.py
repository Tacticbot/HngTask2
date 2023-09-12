from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name: str 
    age: int


app = FastAPI()

@app.post("/api")
async def create_user():
    pass 

@app.get("/")
async def root():
    return {"message":"HNG X task 1, check /api for the task"}

