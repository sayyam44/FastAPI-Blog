from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    #here we are checking the user password that has been hashed is same as 
    #the unhashed version of it that is the hashed password or not
    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)