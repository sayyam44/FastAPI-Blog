from fastapi import FastAPI
from . import  models
from .database import engine
from  .routers import blog, user,authentication

app=FastAPI()

#the below line defines that whenever a new model is created we create that table in database
models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
