from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from .src.user import User 
from .settings.db import BD_URL

# Definir a base para o ORM
Base = declarative_base()

# Definindo conexão com o Banco de Dados:
engine = create_engine(BD_URL, echo= True)

# Criar a tabela no banco de dados (se ela não existir)
Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco
Session = sessionmaker(bind=engine)
session = Session()

class UserManager():
    def __init__(self):
        self.user = User(session)

    def get_all_user(self):
        return self.user.get_all_user()

    def get_by_cpf(self, cpf):
        return self.user.get_user_by_cpf(cpf)