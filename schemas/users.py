from pydantic import BaseModel

class Birthdate(BaseModel):
    date: str

class Register(BaseModel):
    username: str
    password: str
    email: str
    birthdate: Birthdate | None

    