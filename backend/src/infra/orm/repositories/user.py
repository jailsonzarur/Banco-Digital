from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.orm.models import models
from uuid import uuid4
from sqlalchemy import text

class UserRepositorie:

    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: schemas.User):
        user = models.User(id=str(uuid4()), cpf_cnpj=user.cpf_cnpj, 
                           name=user.name, email=user.email, password=user.password)
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user_by_email(self, email: str):
        user = self.db.query(models.User).filter(models.User.email == email).first() 
        return user
    

    
    
         