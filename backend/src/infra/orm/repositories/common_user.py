from src.infra.orm.repositories.user import UserRepositorie
from sqlalchemy.orm import Session
from sqlalchemy import text

class CommonUser(UserRepositorie):

    def __init__(self, db):
        super().__init__(db)
        self.type = "common"

    def trasnferir(self):
        return {"Message": "Fazendo trasnferência"}
    