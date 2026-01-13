import psycopg2

class UserConnection ():
    conn = None
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host ="localhost",
                database ="fastapi_api_publica",
                user ="postgres",
                password = "root",
                port ="5432"
            )
        except psycopg2.OperationalError as err:
            print("Error connection to database: ",err)
            self.conn.close()

    def inser_db (self, data):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                           INSERT INTO "user" (name,age) 
                           VALUES (%(name)s, %(age)s)
                           """,data)
            self.conn.commit()
    def read_db(self):
        with self.conn.cursor() as cursor:
            cursor.execute('SELECT * FROM "user"')
            records = cursor.fetchall()
            return records