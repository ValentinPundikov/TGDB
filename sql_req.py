import sqlite3
import re
import string

connection = sqlite3.connect("DB_NAME.db")
cursor = connection.cursor()


# Внос ID в базу +
# Внос имени в базу +
# Внос возраста в базу +
# Внос числа в базу +
# Изменение имени +
# Изменение даты +
# Изменение числа +
# Получение имени
# Получение возраста
# Получение числа

# Создание базы
def create_database():
    # Создаем таблицу Users.
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, tgid INTEGER, name TEXT, age INTEGER, number INTEGER)')
    connection.commit()


# Внос ID
def set_id(id):
    res = cursor.execute('SELECT CASE WHEN tgid = ? AND name IS NOT NULL THEN 1 ELSE 0 END AS result FROM users;',
                         (id,))
    if res == 1:
        pass
    else:
        cursor.execute('INSERT INTO users (tgid) VALUES (?)', (id,))
        connection.commit()


def add_user(name, id):
    cursor.execute('UPDATE users SET name = ? WHERE tgid = ?', (name, id,))
    connection.commit()


def add_age(id, age):
    cursor.execute('UPDATE users SET age = ? WHERE tgid = ?', (age, id,))
    connection.commit()


def add_number(id, number):
    cursor.execute('UPDATE users SET number = ? WHERE tgid = ?', (number, id,))
    connection.commit()


def set_new_name(name, id):
    name = cursor.execute('UPDATE users SET name = ? WHERE tgid = ?', (name, id,))
    connection.commit()
    return name


def set_new_age(age, id):
    cursor.execute('UPDATE users SET age = ? WHERE tgid = ?', (age, id,))
    connection.commit()


def set_new_number(number, id):
    cursor.execute('UPDATE users SET number = ? WHERE tgid = ?', (number, id,))
    connection.commit()


def get_user(id):
    s1 = re.sub("[,|)|]", "", str(cursor.execute('SELECT name FROM users WHERE tgid=?', (id,)).fetchone()))
    connection.commit()
    return s1



def get_age(id):
    s1 = re.sub("[(|)|,|']", "", str(cursor.execute('SELECT age FROM users WHERE tgid=?', (id,)).fetchone()))
    connection.commit()
    return s1


def get_number(id):
    s1 = re.sub("[(|)|,|']", "", str(cursor.execute('SELECT number FROM users WHERE tgid=?', (id,)).fetchone()))
    connection.commit()
    return s1


def check_id(id):
    vals = str(cursor.execute("SELECT tgid FROM users WHERE tgid=?", (id, )).fetchone())
    #vals = str(vals)
    s1 = re.sub("[(|)|,]", "", vals)
    return s1

