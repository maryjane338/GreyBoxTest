import pytest
import sqlite3
import os


@pytest.fixture
def db_creation_removal():
    if os.path.exists("..\database\\temporary.db"):
        query2 = ''' DELETE FROM Orders '''
    else:
        query2 = ''
    db = sqlite3.connect("..\database\\temporary.db")
    cursor = db.cursor()
    cursor.execute(query2)
    db.commit()
    query = ''' CREATE TABLE IF NOT EXISTS Orders (id_order INTEGER PRIMARY KEY NOT NULL, 
                type_of_work, description, acceptance_date, customer, executor, 
                status) '''
    cursor.execute(query)
    db.commit()
    db.close()

@pytest.fixture
def view_creation():
    if os.path.exists("..\database\\temporary_filter.db"):
        query2 = ''' DELETE FROM Orders '''
    else:
        query2 = ''
    db = sqlite3.connect("..\database\\temporary_filter.db")
    cursor = db.cursor()
    cursor.execute(query2)
    query = ''' CREATE TABLE IF NOT EXISTS Orders (id_order INTEGER PRIMARY KEY NOT NULL, 
                    type_of_work, description, acceptance_date, customer, executor, 
                    status) '''
    cursor.execute(query)
    query_insert = """ INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
                        VALUES ('1', 'Ремонт смартфона', 'Ремонт смартфона (описание)', '2024-10-28', 'Пушкарёв Владислав',
                                'Иванов', 'Принят') """
    query_insert2 = """ INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
                        VALUES ('2', 'Замена экрана ноутбука', 'Замена экрана ноутбука (описание)', '2024-10-29',
                                'Мищенко Никита', 'Сидоров', 'В работе') """
    query_insert3 = """ INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
                        VALUES ('3', 'Установка программного обеспечения', 'Установка программного обеспечения (описание)',
                                '2024-10-30', 'Мейдич Артемий', 'Сидоров', 'Ожидание комплектующих') """
    query_insert4 = """ INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
                        VALUES ('4', 'Чистка от пыли', 'Чистка от пыли (описание)', '2024-10-31', 'Слезов Сергей', 'Петров',
                                'Уточнение информации') """
    query_insert5 = """ INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
                        VALUES ('5', 'Замена батареи', 'Замена батареи (описание)', '2024-11-01', 'Дубина Степан', 'Петров',
                                'Выполнен') """
    cursor.execute(query_insert)
    cursor.execute(query_insert2)
    cursor.execute(query_insert3)
    cursor.execute(query_insert4)
    cursor.execute(query_insert5)
    query_view = '''CREATE VIEW IF NOT EXISTS orders_with_filter AS
                        SELECT Orders.id_order,  Orders.description, Orders.acceptance_date, Orders.customer
                        FROM Orders'''
    cursor.execute(query_view)
    db.commit()
    db.close()
