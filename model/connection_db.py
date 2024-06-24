import psycopg2

class UserConnection:
    def __init__(self):
        try: 
            self.conn = psycopg2.connect("dbname=tic user=postgres password=tic1234 host=localhost port=5432")
        except psycopg2.OperationalError as err:
            print(err)
            if self.conn is not None:
                self.conn.close()

    def __del__(self):
        if self.conn is not None:
            self.conn.close()
