from model.connection_db import UserConnection

from fastapi import HTTPException


class UserController:
    def __init__(self):
        self.conn = UserConnection()

    def write(self, data):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("""
                INSERT INTO "people"(name, last_name, type_of_user, post, office, user_name, password) 
                VALUES(%(name)s, %(last_name)s, %(type_of_user)s, %(post)s,%(office)s,%(user_name)s,%(password)s)""",data)
            self.conn.conn.commit()
            return {"message": "Data inserted successfully"}
        except Exception as e:
            raise e

    def read(self, user_id):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("SELECT * FROM people WHERE id = %s", (user_id,))
                user = cur.fetchone()
                if user:
                    return {
                        "id": user[0],
                        "name": user[1],
                        "last_name": user[2],
                        "type_of_user": user[3],
                        "post": user[4],
                        "office": user[5],
                        "user_name": user[6],
                        "password": user[7]
                    }
                else:
                    raise HTTPException(status_code=404, detail="User not found")
        except Exception as e:
            raise e

    def update(self, user_id, data):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("""
                UPDATE people 
                SET name=%(name)s, last_name=%(last_name)s, type_of_user=%(type_of_user)s, 
                post=%(post)s, office=%(office)s, user_name=%(user_name)s, password=%(password)s
                WHERE id=%(id)s""", {**data, "id": user_id})
            self.conn.conn.commit()
            return {"message": "User updated successfully"}
        except Exception as e:
            raise e

    def delete(self, user_id):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("DELETE FROM people WHERE id = %s", (user_id,))
            self.conn.conn.commit()
            return {"message": "User deleted successfully"}
        except Exception as e:
            raise e
        
    def get_all_users(self):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("SELECT * FROM people")
                users = cur.fetchall()
                user_list = []
                for user in users:
                    user_list.append({
                        "id": user[0],
                        "name": user[1],
                        "last_name": user[2],
                        "type_of_user": user[3],
                        "post": user[4],
                        "office": user[5],
                        "user_name": user[6],
                        "password": user[7]
                    })
                return user_list
        except Exception as e:
            raise e
