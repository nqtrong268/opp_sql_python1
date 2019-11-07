import psycopg2


class Football:

    def __init__(self, database, user, psw, port='5432', host='localhost'):
        """
        :param database: database
        :param user:  username database
        :param psw:  password database
        :param port: port connection database
        :param host: host connection database
        """
        self.database = database
        self.user = user
        self. psw = psw
        self.port = port
        self.host = host

    def get_connect(self):
        """
        :return:  cursor obj
        """

        try:
            self.conn = psycopg2.connect(
                host=self.host,
                user=self.user,
                password=self.psw,
                port=self.port,
                database=self.database
            )
            self.cr = self.conn.cursor()

        except(Exception, psycopg2.DatabaseError) as error:
            print('Erron when connect database', error)

    def creat_table(self, sql):
        self.cr.execute(sql)
        self.conn.commit()

    def close_data(self):
        self.cr.close()

    def insert_data(self, sql):
        self.cr.execute(sql)
        self.conn.commit()

    def select_data(self, slc):
        self.cr.execute(slc)
        resule = self.cr.fetchall()
        return resule


connect_db = Football('baitap_psycopg2', 'postgres', 'trong234')
connect_db.get_connect()

sql = """
    CREATE TABLE club (
        id SERIAL PRIMARY KEY,
        name VARCHAR,
        year INTEGER
    )
"""

sql1 = """
    CREATE TABLE country (
        id SERIAL PRIMARY KEY,
        name VARCHAR
    )
"""

sql2 = """
    CREATE TABLE player(
        id SERIAL PRIMARY  KEY,
        name VARCHAR,
        age INTEGER,
        club_id INTEGER REFERENCES club(id),
        country_id INTEGER REFERENCES country(id)
    )
"""

# connect_db.creat_table(sql)
# connect_db.creat_table(sql1)
# connect_db.creat_table(sql2)

# connect_db.close_data()

# data = """
#     INSERT INTO club(name, year) values ('{name}', '{year}')
# """.format(name='Real', year=1901)

data1 = """
    INSERT INTO COUNTRY(NAME) VALUES ('Spain'), ('Argentina'), ('Portugal')
"""

data2 = """
    INSERT INTO player(name, age, club_id, country_id) VALUES ('Ramos', 26, 1, 1),
                                                              ('Ronado', 31, 1, 1),
                                                              ('Messi', 29, 3, 2),
                                                              ('Cesc', 31, 2, 1),
                                                              ('Alba', 27, 3, 1)
"""

# connect_db.insert_data(data)
# connect_db.insert_data(data1)
# connect_db.insert_data(data2)

slc = """
    select p.name, c.name from player p
    inner join club c 
    on p.club_id = c.id
    order by c.name
"""

# resule = connect_db.select_data(slc)
#
# for ct in resule:
#     print('Name is %s - club: %s' %ct)

# Viết hàm python để lấy ra thông tin: Tên cầu thủ, tuổi cầu thủ, tên quốc tịch của các
# cầu thủ đang chơi cho câu lạc bộ Barcelona, sắp xếp thứ tự tăng dần theo tên cầu thủ.

slc1 = """
    select p.name, p.age, c.name 
    from player p
    inner join club cl 
    on cl.id = p.club_id
    inner join country c
    on c.id = p.country_id
    where cl.name = 'Barcelona'
    order by p.name 
"""

# resule = connect_db.select_data(slc1)
#
# for ct in resule:
#     print('Name is %s - tuổi: %s - Quốc tịch: %s ' %ct)

# Viết hàm python để lấy ra thông tin: Tên cầu thủ, tuổi cầu thủ, tên câu lạc bộ, tên
# quốc tịch của các cầu thủ có tuổi nhỏ hơn 30, sắp xếp thứ tự tăng dần theo tên câu lạc bộ.

slc2 = """
    SELECT p.name, p.age, cl.name, c.name 
    FROM player p 
    LEFT JOIN club cl 
    ON cl.id = p.club_id
    LEFT JOIN country c 
    on c.id = p.country_id
    WHERE p.age < 30
    ORDER BY cl.name
"""
resule = connect_db.select_data(slc2)

for ct in resule:
    print('Name is %s - tuổi: %s - Câu lạc bộ: %s - Quốc tịch: %s ' %ct)