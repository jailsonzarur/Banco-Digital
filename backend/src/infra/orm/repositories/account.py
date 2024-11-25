from src.infra.orm.models import models
from sqlalchemy import text
from uuid import uuid4

class Account:

    def __init__(self, db, type):
        self.db = db
        self.type = type 

    def create_account(self, user_id):
        self.db.execute(text("INSERT INTO accounts (id, user_id, ammount, type_account, is_activate) VALUES \
                             (:value1, :value2, :value3, :value4, :value5)"), 
                             {"value1": str(uuid4()), "value2": user_id, "value3": 0.0,
                              "value4": self.type, "value5": True})
        self.db.commit()

    def get_balance(self, user_id):
        pass

    
