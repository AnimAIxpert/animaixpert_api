from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from utils.api import USER_MS_URL
import httpx

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def validate_token(token: str = Depends(oauth2_scheme)):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    async with httpx.AsyncClient() as client:
        ans = httpx.get(USER_MS_URL + "/user", headers=headers)
    if ans.status_code != 200:
        raise Exception("Invalid token")
    return True