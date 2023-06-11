from fastapi import APIRouter
from utils.api import CATALOGUE_MS_URL
import httpx

router = APIRouter()

@router.get("/anime")
async def get_anime(id: int):
    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(CATALOGUE_MS_URL + f"/anime?id={id}", headers=headers)
    return ans.json()

@router.get("/anime-by-genre")
async def get_animes(genre: str, limit: int | None = None):
    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(CATALOGUE_MS_URL + f"/anime-by-genre?genre={genre}&limit={limit}", headers=headers)
    return ans.json()

@router.get("/anime-top")
async def get_animes_top(limit: int | None = None, genre: str | None = None):
    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(CATALOGUE_MS_URL + f"/anime-top?limit={limit}&genre={genre}", headers=headers)
    return ans.json()

