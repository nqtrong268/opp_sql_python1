import  psycopg2
from buoi13_trenlop import Psyconnect


class creates_tb(Psyconnect):

    def __init__(self):
        self.connect_db = Psyconnect('buoi13_trenlop', 'postgres', 'trong234', '5432', 'localhost')
        self.connect_db.get_connect()

    def create_tb_club(self):
        crt = """
            CREATE TABLE IF NOT EXISTS club (
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                years INTEGER DEFAULT '1980'
            )
        """
        self.connect_db.cr.execute(crt)
        self.connect_db.conn.commit()

    def create_tb_country(self):
        crt1 = """
            CREATE TABLE IF NOT EXISTS country (
                id SERIAL PRIMARY KEY,
                name VARCHAR
            )
        """
        self.connect_db.cr.execute(crt1)
        self.connect_db.conn.commit()

    def create_tb_player(self):
        crt2 = """
            CREATE TABLE player(
                id SERIAL PRIMARY  KEY,
                name VARCHAR,
                age INTEGER,
                club_id INTEGER REFERENCES club(id),
                country_id INTEGER REFERENCES country(id)
            )
        """
        self.connect_db.cr.execute(crt2)
        self.connect_db.conn.commit()


conn1 = creates_tb()
conn1.create_tb_club()
conn1.create_tb_country()
conn1.create_tb_player()
# connect_db.create_tb(crt)