from database import get_connection

def search_user_by_email(email: str):
    """
        search for a user in the database by mail
    """
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(f"select * from user where user_email = '{email}';")
    user_result = cursor.fetchall()

    cursor.close()
    connection.close()

    return user_result
