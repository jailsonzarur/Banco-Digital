from fastapi import FastAPI, Depends
from src.infra.orm.repositories.common_user import CommonUser
from src.infra.orm.repositories.storekeeper_user import StoreKeeperUser
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.orm.config.database import get_db, create_db

app = FastAPI()

@app.get('/')
def health_check():
    return {"Message": "OK!"}

@app.post('/')
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    common_user = CommonUser(db).create_user(user)
    return common_user
