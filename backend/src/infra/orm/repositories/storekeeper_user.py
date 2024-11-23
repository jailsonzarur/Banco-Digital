from src.infra.orm.repositories.user import UserRepositorie
from sqlalchemy import text

class StoreKeeperUser(UserRepositorie):

    def __init__(self, db):
        super().__init__(db)
        self.type = "storekeeper"

    def trasnferir(self):
        return {"Message": "Você é um lojista, você não pode fazer transferências"}
    
