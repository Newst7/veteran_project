import sqlite3

conn = sqlite3.connect(r'C:\Users\User\Documents\GitHub\veteran_project\project_flask/myDB.db')
cur = conn.cursor()
i = 0

print('Имя')
name = input()
print('Фамилия')
secName = input()
print('Город')
city = input()
print('Электронная Почта')
email = input()
print('Пароль')
passwd = input()
print('Повтор пароля')
repeatPasswd = input()

if (passwd != repeatPasswd):
    print('Неверно введён пароль')
else:
    i = i +1
    aaa = (i, name, secName, city, email, passwd)
    cur.execute("INSERT INTO user VALUES(?, ?, ?, ?, ?, ?);", aaa)
    conn.commit()
# типа в бд всё заносим если всё верно
