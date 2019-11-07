import psycopg2


class ConnectPostgress:

    def __init__(self, db_name, user, pwd, port='5432', host='localhost'):
        """
        :param db_name:
        :param user:
        :param pwd:
        :param port:
        :param host:
        """
        self.db_name = db_name
        self.user = user
        self.pwd = pwd
        self.port = port
        self.host = host

    def get_connection(self):
        """
        :return: cursor obj
        """
        try:
            self.conn =psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.pwd,
                port=self.port,
                database=self.db_name
            )
            self.cr = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print('Error when connect database', error)

    def insert_data(self, sql):
        self.cr.execute(sql)
        self.conn.commit()
        self.cr.close()

    def select_data(self, sql):
        self.cr.execute(sql)
        resule = self.cr.fetchall()
        self.cr.close()
        return resule


    def select_data2(self, sql):
        self.cr.execute(sql)
        resule = self.cr.fetchone()
        return resule


connect_db = ConnectPostgress('buoi11_trenlop', 'postgres', 'trong234')
connect_db.get_connection()
# sql = """
#     CREATE TABLE employee(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR NOT NULL,
#         phone VARCHAR,
#         address VARCHAR
#     )
# """

# sql = """
#     INSERT INTO employee(name, phone, address) VALUES ('{name}','{phone}','{address}')
# """.format(phone = '0974013092', name = 'Trọng đại ca', address= 'Hải Dương')

# sql = """
#     UPDATE employee SET phone = '03647238' WHERE  ID = 1
# """
sql = """
    SELECT name, phone FROM employee LIMIT 1
"""

resule = connect_db.select_data2(sql)
print(resule)
print('name is %s - phone is %s' %resule)
# for emp in resule:
#     print("Name is %s - Phone is %s" %emp)





