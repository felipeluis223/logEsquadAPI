from sqlalchemy import Column, String, Date
from sqlalchemy.ext.declarative import declarative_base

# Definir a base para o ORM
Base = declarative_base()

# Tabela de usuário:
class UserModel(Base):
    __tablename__ = 'users'

    cpf = Column(String(11), primary_key=True)
    nome = Column(String(100), nullable=False)
    telefone = Column(String(15), nullable=False)
    email = Column(String(100), nullable=False)
    rg = Column(String(20), nullable=False)
    data_nascimento = Column(Date, nullable=False)

    def to_dict(self):
        return {
            'cpf': self.cpf,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'rg': self.rg,
            'data_nascimento': self.data_nascimento.isoformat()  # Converter a data para string no formato ISO
        }