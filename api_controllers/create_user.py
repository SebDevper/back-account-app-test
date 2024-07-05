from models.user import User
from database import get_connection
from db_actions.search_user import search_user_by_email
from db_actions.insert_user import insert_new_user_db

def create_new_user(user: User):
    """
        insert new user if not exist already
    """

    if search_user_by_email(user.user_email):
        return {'code': 0, 'error': 'email ya en uso'}

    insert_result = insert_new_user_db(user)
    if insert_result > 0:
        return {'code': 2, 'message': 'user inserted'}
    
    return {'code': -1, 'message': 'insertion error'}
