from pydantic import BaseModel

class UserLogin(BaseModel):
    user_email: str
    user_key: str
