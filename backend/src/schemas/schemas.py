from pydantic import BaseModel

class User( BaseModel ):
    cpf_cnpj: str
    name: str
    email: str
    password: str
