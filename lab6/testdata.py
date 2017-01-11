import MySQLdb

#Открываем соединение
db = MySQLdb.connect(
    host="localhost",
    user="dbuser",
    passwd="123",
    db="first_db",
    charset="utf8"
)

#Получаем курсор для работы с БД
c = db.cursor()
#Выполняем вставку
c.execute("INSERT INTO books (name, description) VALUES (%s, %s);",('Книга', 'Описание книги'))

#Фиксируем изменеия
db.commit()
#Выполняем выборку
c.execute("SELECT * FROM books")
#Забираем все полученные записи
entries = c.fetchall()
#И печатаем их
for e in entries:
    print(e)

c.execute("DELETE FROM books WHERE id>1")
db.commit()

c.close()  #Закрываем курсор
db.close() #Закрываем соединение