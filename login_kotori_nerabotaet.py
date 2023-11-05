import sqlite3

def user_check(login,cursor):
    cursor.execute('SELECT * FROM LOSERS')
    users = cursor.fetchall()
    print (users)

    counter=0
    for user in users:
        for name in user:
            if name == login:
                counter+=1
    return counter

       

def counter_(a):
    if a>=1:
       return('est')
    elif a<1:
        print('u need zaregacca')
        login=input('pishi login ')
        password=input('a teper parol ')
        cursor.execute('INSERT INTO LOSERS(username,password) VALUES(?,?)',(login,password))
        return('molodec')

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
login=input()
# Выбираем всех пользователей
a=user_check

print(counter_)


connection.commit()
connection.close()