from database import get_connection
from datetime import datetime

def save_token_to_db(user_id: int, token: str):
    """
    save a token to the database
    """

    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"""
        insert into user_token 
        (user_id, token) 
        values ('{user_id}', '{token}');
    """)
    insert_result = cursor.rowcount
    connection.commit()
    cursor.close()
    connection.close()

    return insert_result

def get_token(token: str):
    """
    check if token exists in the DB
    """

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"""
        select * from user_token 
            where token = '{token}' 
        ;""")
    user_result = cursor.fetchall()

    cursor.close()
    connection.close()

    return user_result
