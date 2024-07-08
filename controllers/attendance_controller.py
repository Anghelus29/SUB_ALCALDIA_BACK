from model.connection_db import UserConnection

#Metodo pàra registrar la solicitud de ayuda
class AttendanceController:
    def __init__(self):
        self.conn = UserConnection()

    def insert_attendance(self, attendance_data):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO attendance (id_people, hardware, software, description, date, hour, state)
                    VALUES (%(id_people)s, %(hardware)s, %(software)s, %(description)s, %(date)s, %(hour)s, %(state)s)""", attendance_data)
                self.conn.conn.commit()
                return {"message": "Data inserted successfully"}
        except Exception as e:
            raise e

    #Metodo para mostrar todas las solicitudes
    def get_all_requests(self):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("SELECT attendance.id AS attendance_id, attendance.id_people, attendance.hardware, attendance.software, attendance.description, attendance.date, attendance.hour, attendance.state, people.id AS people_id, people.name, people.last_name, people.type_of_user, people.post, people.office, people.user_name FROM attendance JOIN  people ON attendance.id_people = people.id; ")
                attendances=cur.fetchall()
                attendance_list=[]
                for attendance in attendances:
                    attendance_list.append({
                        "id": attendance[0],
                        "id_people": attendance[1],
                        "hardware": attendance[2],
                        "software" : attendance[3],
                        "description" : attendance[4],
                        "date" : attendance[5],
                        "hour" : attendance[6],
                        "state" : attendance[7],
                        "people_id" : attendance[8],
                        "name" :  attendance[9],
                        "last_name" : attendance[10],
                        "type_of_user" : attendance[11],
                        "post" : attendance[12],
                        "office" : attendance[13],
                        "user_name" : attendance[14]
                    })       
                return attendance_list
        except Exception as e:
            raise e
