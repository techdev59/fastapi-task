from pydantic import BaseModel, EmailStr, constr

class UserCreate(BaseModel):
    email: EmailStr
    password: constr(min_length=8)

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True

class PostCreate(BaseModel):
    text: constr(max_length=1024)

class Post(BaseModel):
    id: int
    text: str
    owner_id: int

    class Config:
        from_attributes = True
