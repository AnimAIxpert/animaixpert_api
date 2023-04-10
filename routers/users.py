from fastapi import APIRouter, Depends
from utils.api import USER_MS_URL
from schemas.users import *
import httpx

router = APIRouter()

@router.get("/login")
async def login(username: str, password: str):
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "username": username,
        "password": password
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.post(USER_MS_URL + "/login", json=body, headers=headers) 
    return ans.json()

@router.get("/register")
async def register(Register: Register):
    return Register
