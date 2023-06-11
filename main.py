# uvicorn main:app --reload --port 8001
import os
from fastapi import FastAPI
from routers import users, catalogue, rating
from fastapi.middleware.cors import CORSMiddleware
from utils.api import origins


# APP
app = FastAPI()

app.include_router(users.router)
app.include_router(catalogue.router)
app.include_router(rating.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello This is AnimAIxpert's API"}
