from fastapi import APIRouter, Depends,status,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas,database,models,token
from sqlalchemy.orm import Session
from ..hashing import Hash
router = APIRouter(tags=['Authentication'])

@router.post('/login')
# request:schemas.Login-> It defines the schemas for username and password
def login(request:OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(database.get_db)):
    #the username is the email of the user 
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")
    
    #as we are fetching the user on the basis of the email id not the username
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}