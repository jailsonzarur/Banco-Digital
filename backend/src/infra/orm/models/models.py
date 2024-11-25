from src.infra.orm.config.database import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey

# Usuário
class User( Base ):
    __tablename__ = "users"

    #CPF e EMAIL são únicos por Usuário
    id: Mapped[str] = mapped_column(primary_key=True)
    cpf_cnpj: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

class Account ( Base ):
    __tablename__ = "accounts"

    id: Mapped[str] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"), unique=True)
    ammount: Mapped[float] = mapped_column(nullable=False, default=0.0)
    type_account: Mapped[str] = mapped_column(nullable=False)
    is_activate: Mapped[bool] = mapped_column(nullable=False, default=True)

# Note que, um usuário e lojista serão registrados na mesma tabela accounts
# de banco de dados(Single Table Inheritance). Como a única de diferença 
# entre eles será o método de tranferência, 
# é mais ágil(Tanto em implementação como em consulta) adotar esse método,

