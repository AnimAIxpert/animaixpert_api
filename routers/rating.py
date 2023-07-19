from fastapi import APIRouter
from utils.api import RATING_MS_URL
from schemas.rating import Rating
import httpx

router = APIRouter()

@router.get("/get-rating-by-ids")
async def get_anime(user_id: str , anime_id: int):
    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(RATING_MS_URL + f"/get-rating-by-ids?user_id={user_id}&anime_id={anime_id}", headers=headers)
    return ans.json()

@router.post("/create-rating")
async def get_animes(rating: Rating):
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "user_id": rating.user_id,
        "anime_id": rating.anime_id,
        "rating": rating.rating
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.post(RATING_MS_URL + f"/create-rating", json=body, headers=headers)
    return ans.json()

@router.get("/get-rating")
async def get_animes_top():
    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(RATING_MS_URL + f"/get-rating", headers=headers)
    return ans.json()

@router.get("/get-ratings-by-user")
async def get_animes_top(user_id: str):
    headers = {
        "Content-Type": "application/json"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(RATING_MS_URL + f"/get-ratings-by-user?user_id={user_id}", headers=headers)
    return ans.json()

