import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente .env:
load_dotenv()


# Definir configuração do BD:
dataBD = {
    "host": os.getenv('HOST'),
    "database": os.getenv('DATABASE'),
    "user": os.getenv('USER'),
    "password": os.getenv('PASSWORD'),
    "port": os.getenv('PORT')
}

# Definindo conexão com o Banco de Dados:
BD_URL = f'postgresql://{dataBD["user"]}:{dataBD["password"]}@{dataBD["host"]}:{dataBD["port"]}/{dataBD["database"]}'
