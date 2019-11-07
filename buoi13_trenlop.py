import psycopg2


class Psyconnect:

    def __init__(self, db_name, name, psw, port='5432', host='localhost'):
        """"
        :param db: database database
        :param name: username database
        :param psw: password database
        :param port: port database
        :param host: host database
        """
        self.db_name = db_name
        self.name = name
        self.psw = psw
        self.port = port
        self.host = host

    def get_connect(self):
        """
        :return:
        """
        try:
            self.conn = psycopg2.connect(
                database=self.db_name,
                host=self.host,
                user=self.name,
                password=self.psw,
                port=self.port
            )
            self.cr = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error when connect database ", error)

    def get_close(self):
        self.conn.close()

# connect_db = Psyconnect('buoi13_trenlop','postgres','trong234')
# connect_db.get_connect()