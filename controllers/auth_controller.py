from model.connection_db import UserConnection

class AuthController:
    def __init__(self):
        self.conn = UserConnection()

    def authenticate_user(self, username: str, password: str):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("""
                SELECT * FROM "people" WHERE user_name = %(username)s AND password = %(password)s;
                """, {'username': username, 'password': password})
                user_data = cur.fetchone()
                if user_data:
                    return {"id": user_data[0], "name": user_data[1], "last_name": user_data[2], "type_of_user": user_data[3], "post": user_data[4], "office": user_data[5]}
                else:
                    return None
        except Exception as e:
            raise e
