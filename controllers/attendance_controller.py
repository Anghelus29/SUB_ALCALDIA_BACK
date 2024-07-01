from model.connection_db import UserConnection

class AttendanceController:
    def __init__(self):
        self.conn = UserConnection()

    def insert_attendance(self, attendance_data):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO attendance (id_people, hardware, software, description)
                    VALUES (%(id_people)s, %(hardware)s, %(software)s, %(description)s)""", attendance_data)
                self.conn.conn.commit()
                return {"message": "Data inserted successfully"}
        except Exception as e:
            raise e
