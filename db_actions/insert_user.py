from database import get_connection
from models.user import User

def insert_new_user_db(user: User):
    """
        insert a new user in the database
    """
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
        insert into user 
        (user_name, user_email, user_key) 
        values ('{user.user_name}', '{user.user_email}', '{user.user_key}');
    """)
    insert_result = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()

    return insert_result
