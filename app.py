from flask import Flask, jsonify
from db.index import UserManager


# Criar instância da aplicação:
app = Flask(__name__)

use_manager = UserManager()

# Definindo rotas:
@app.route('/')
def main():
    return 'Welcome in LOGESQUAD'


# Rotas de usuários do sistema:
@app.route('/user/all')
def get_all_user():
    users_data = use_manager.get_all_user()
    if 'data' in users_data:
        return jsonify(users_data['data'])
    else:
        return 'Nenhum usuário encontrado'

@app.route("/user/<cpf>")
def user(cpf):
    user_by_cpf = use_manager.get_by_cpf(cpf)
    try: 
        return jsonify(user_by_cpf['data'])
    except:
        return jsonify(user_by_cpf['error'])

# Verifica se o script está sendo executado diretamente e roda o servidor:
if __name__ == '__main__':
    app.run(debug=True)