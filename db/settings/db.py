# Definir configuração do BD:
dataBD = {
    "host": "localhost",
    "database": "logesquad",
    "user": "postgres",
    "password": "dqm50vnc",
    "port": 5432
}

# Definindo conexão com o Banco de Dados:
BD_URL = f'postgresql://{dataBD["user"]}:{dataBD["password"]}@{dataBD["host"]}:{dataBD["port"]}/{dataBD["database"]}'