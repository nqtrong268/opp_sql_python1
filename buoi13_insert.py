import psycopg2
from buoi13_trenlop import Psyconnect


class bai13_insert(Psyconnect):

    def __init__(self):
        self.connect_insert = Psyconnect('buoi13_trenlop', 'postgres', 'trong234', '5432', 'localhost')
        self.connect_insert.get_connect()

    def insert_db_country(self):
        data = """
            INSERT INTO COUNTRY(NAME) VALUES ('Spain'), ('Argentina'), ('Portugal')
        """
        self.connect_insert.cr.execute(data)
        self.connect_insert.conn.commit()




# data2 = """
#     INSERT INTO player(name, age, club_id, country_id) VALUES ()
# """

insert1 = bai13_insert()
insert1.insert_db_country()
# connect_db_insert.get_connect()
# connect_db_insert.inser_db()