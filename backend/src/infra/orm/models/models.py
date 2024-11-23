from src.infra.orm.config.database import Base
from sqlalchemy.orm import mapped_column, Mapped

# Usuário
class User( Base ):
    __tablename__ = "users"

    #CPF e EMAIL são únicos por Usuário
    id: Mapped[str] = mapped_column(primary_key=True)
    cpf_cnpj: Mapped[str] = mapped_column(nullable=False, unique=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)

# Note que, um usuário e lojista serão registrados na mesma tabela 
# de banco de dados(Single Table Inheritance). Como a única de diferença 
# entre eles será o método de tranferência, 
# é mais ágil(Tanto em implementação como em consulta) adotar esse método,

