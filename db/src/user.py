from ..models.users import UserModel

class User():
    def __init__(self, session):
        self.session = session

    # Obter informações de todos os usuários cadastrados no sistema:
    def get_all_user(self):
        users = self.session.query(UserModel).all()
        try:
            users_data = [user.to_dict() for user in users]
            return {'data': users_data}
        except:
            pass
    
    # Obter dados de um usuário específico através do CPF:
    def get_user_by_cpf(self, cpf):
        # Filtrando pelo campo de CPF:
        user = self.session.query(UserModel).filter(UserModel.cpf == cpf).first()
        try:
            if user is None:
                return {'error': 'Usuario nao encontrado para o CPF fornecido.'}
            
            # Se o usuário for encontrado, retorna seus dados convertidos para dicionário
            return {'data': user.to_dict()}
        
        except Exception as error: 
            print(error)