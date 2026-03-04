from pydantic import BaseModel, Field

class User(BaseModel):
    password: str = Field(..., repr=False)
    login: str