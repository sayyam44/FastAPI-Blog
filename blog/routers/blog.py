from fastapi import APIRouter,Depends,status,HTTPException
from .. import schemas,database,models, oauth2
from typing import List
from sqlalchemy.orm import Session
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

get_db=database.get_db

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
#db:Session=Depends(get_db) -> Creating the instance of database i.e.
# to define db and it is a type of session andit default value depends aupon get_db 
#we use request: schemas.Blog whenever we need to pass anything from db to the user eg in create or update
def create(request: schemas.Blog,db:Session=Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id:int,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request:schemas.Blog,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id,request, db)

#response_model=schemas.ShowBlog -> If we want to get a particular type of response from pydantic model schemas
@router.get('/{id}',status_code=200,response_model=schemas.ShowBlog)
def show(id:int,db:Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id,db)
