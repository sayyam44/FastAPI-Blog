from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get('/blog')
def index(limit=10,published: bool = True, sort:Optional[str]=None):
    if published:
        return {'data':f'blog list of {limit} noooo'}
    else:
        return {'data':f'blog list of {limit} yesssssss'} 


@app.get('/blog/{id}')
def index(id:int):
        return {'data':id}

@app.get('/blog/{id}/comments')
def index(id):
        return {'data':{'1','2'}}

class Blog(BaseModel):
    title: str
    body: str
    published:Optional[bool]

@app.post('/blog')
def create_blog(request:Blog):
        return {'data':"Blog is created"}
