from pydantic import BaseModel

class Rating(BaseModel):
    user_id: str
    anime_id: int
    rating: int

    