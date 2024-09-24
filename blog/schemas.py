#schemas are the pydantic schemas that defines the 
#the schemas we need for different tasks either 
#to return or to fetch 
from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
    title:str
    body:str

class Blog(BlogBase):
    class Config():
        orm_mode=True

class User(BaseModel):
    name:str
    email:str
    password:str


class ShowUser(BaseModel):
    name:str
    email:str
    blogs: List[Blog]=[]
    class Config():
        orm_mode=True

#this schema is to return the reposne in particular format
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser
    class Config():
        orm_mode=True

    
class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
   email: Optional[str] = None