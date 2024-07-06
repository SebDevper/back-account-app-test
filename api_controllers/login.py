from models.userlogin import UserLogin
from db_actions.search_user import search_user_by_login_data
from db_actions.token import save_token_to_db
import secrets

def login(user_login: UserLogin):
    """
    Login api, generate token to user 
    """
    # check if user and key
    user_found = search_user_by_login_data(user_login.user_email, user_login.user_key)
    if not user_found:
        return {'status': -1, 'message': 'usuario o contraseña incorrectos'}

    # generate token
    token = secrets.token_hex(10)

    # save token
    save_token_to_db(user_found[0][0], token)

    # return token
    return {'status': 0, 'token': token}
