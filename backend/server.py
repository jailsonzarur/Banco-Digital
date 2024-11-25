from fastapi import FastAPI, Depends
from src.infra.orm.repositories.user import UserRepositorie
from src.schemas import schemas
from sqlalchemy.orm import Session
from src.infra.orm.config.database import get_db, create_db
from src.infra.orm.repositories.user import UserRepositorie
from src.infra.orm.repositories.account import Account

app = FastAPI()
create_db()

@app.get('/')
def health_check():
    return {"Message": "OK!"}

@app.post('/create')
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    user = UserRepositorie(db).create_user(user)
    return {"Message": "Usuário criado com sucesso"}

@app.post('/account')
def create_account(user_id: str, db: Session = Depends(get_db)):
    account = Account(db, "common")
    account.create_account(user_id)
    return {"Message": "conta criada com sucesso!"}


