from model.connection_db import UserConnection

class ReportController:
    def __init__(self):
        self.conn = UserConnection()

    def get_all_reports(self):
        try:
            with self.conn.conn.cursor() as cur:
                cur.execute("""
                    SELECT 
                        reports.id AS report_id,
                        people.name,
                        people.last_name,
                        people.post,
                        people.office,
                        attendance.date,
                        attendance.hardware,
                        attendance.software,
                        attendance.description,
                        attendance.date AS attendance_date,
                        attendance.state,
                        reports.date_review,
                        reports.work_done
                    FROM 
                        reports
                    JOIN 
                        attendance ON reports.id_attendance = attendance.id
                    JOIN 
                        people ON attendance.id_people = people.id;
                """)
                
                reports = cur.fetchall()
                report_list = []
                for report in reports:
                    report_list.append({
                        "id": report[0],
                        "name": report[1],
                        "last_name": report[2],
                        "post": report[3],
                        "office": report[4],
                        "date": report[5],
                        "hardware": report[6],
                        "software": report[7],
                        "description": report[8],
                        "attendance_date": report[9],
                        "state": report[10],
                        "date_review": report[11],
                        "work_done": report[12]
                    })       
                return report_list
        except Exception as e:
            raise e
