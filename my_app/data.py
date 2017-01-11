import MySQLdb

class Connection:
    def __init__(self, user, password, db, host='localhost'):
        self.user = user
        self.host = host
        self.password = password
        self.db = db
        self._connection = None

    @property
    def connection(self):
        return self._connection

    def __enter__(self):
        self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()

    def connect(self):
        if not self._connection:
            self._connection = MySQLdb.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db,
                charset = "utf8"
            )

    def disconnect(self):
        if self._connection:
            self._connection.close()

class User:

    def __init__(self, db_connection, username, first_name, last_name, middle_name, birthday, email, phone, sex):
        self.db_connection = db_connection.connection
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.birthday = birthday
        self.email = email
        self.phone = phone
        self.sex = sex

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO my_app_user (username, first_name, last_name, middle_name, birthday, email, phone, sex) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                  (self.username, self.first_name, self.last_name, self.middle_name, self.birthday, self.email, self.phone, self.sex))
        self.db_connection.commit()
        c.close()

    def get(self):
        c = self.db_connection.cursor()
        c.execute("SELECT * FROM my_app_user;")
        users = []
        for row in c.fetchall():
            u = User
            u.username = row[1]
            u.first_name = row[2]
            u.last_name = row[3]
            u.middle_name = row[4]
            u.birthday = row[5]
            u.email = row[6]
            u.phone = row[7]
            u.sex = row[8]
            users.append(u)
        return users

class Computer:
    def __init__(self, db_connection, name, image, description, price):
        self.db_connection = db_connection.connection
        self.name = name
        self.image = image
        self.description = description
        self.price = price

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO my_app_computer (name, images, description, price) VALUES (%s, %s, %s, %s);",
                  (self.name, self.image, self.description, self.price))
        self.db_connection.commit()
        c.close()

class Order:
    def __init__(self, db_connection, adress, delivery_date, count, user_id, computer_id):
        self.db_connection = db_connection.connection
        self.adress = adress
        self.delivery_date = delivery_date
        self.count = count
        self.user_id = user_id
        self.computer_id = computer_id

    def save(self):
        c = self.db_connection.cursor()
        c.execute("INSERT INTO my_app_order (adress, delivery_date, count, user_id, bank_id) VALUES (%s, %s, %s, %s);",
                  (self.adress, self.delivery_date, self.count, self.user_id, self.computer_id))
        self.db_connection.commit()
        c.close()


con = Connection("lab6user", "12345", "lab6_db")

with con:
    user = User(con, 'test_user', 'Ореликов'.encode('utf-8'), 'Михаил'.encode('utf-8'), 'Геннадьевич'.encode('utf-8'), '1997-02-27', 'mymail@mail.ru', '79998887766','М'.encode('utf-8'))
    user.save()
    user = User(con, 'user1', 'Иванов'.encode('utf-8'), 'Иван'.encode('utf-8'), 'Иванович'.encode('utf-8'), '2016-12-23', 'hismail@mail.ru', '78887776655', 'М'.encode('utf-8'))
    user.save()
    #computer = Computer(con, '15.6" Ноутбук Lenovo B5010 черный'.encode('utf-8'), , 'Адрес!')
    #computer.save()
    #computer = Computer()
    #computer.save()
    #order = Order()
    #order.save()