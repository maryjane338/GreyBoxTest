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

@pytest.fixture
def full_db():
    if os.path.exists("..\database\\temporary_full.db"):
        query = ''' DELETE FROM Employees '''
        query2 = ''' DELETE FROM Orders '''
        query3 = ''' DELETE FROM Statuses '''
        query4 = ''' DELETE FROM Works '''
    else:
        query = ''
        query2 = ''
        query3 = ''
        query4 = ''
    db = sqlite3.connect("..\database\\temporary_full.db")
    cursor = db.cursor()
    cursor.execute(query)
    cursor.execute(query2)
    cursor.execute(query3)
    cursor.execute(query4)
    query_employees = '''
                        CREATE TABLE IF NOT EXISTS Employees (
        id_employee INTEGER PRIMARY KEY AUTOINCREMENT
                            NOT NULL,
        surname     TEXT
    )
    '''
    query_orders = '''
    CREATE TABLE IF NOT EXISTS Orders (
        id_order        INTEGER PRIMARY KEY AUTOINCREMENT
                                NOT NULL,
        type_of_work    INTEGER REFERENCES Works (id_work),
        description     TEXT,
        acceptance_date TEXT,
        customer        TEXT,
        executor        INTEGER REFERENCES Employees (id_employee),
        status          INTEGER REFERENCES Statuses (id_status) 
    )
    '''
    query_statuses = '''
    CREATE TABLE IF NOT EXISTS Statuses (
        id_status INTEGER PRIMARY KEY AUTOINCREMENT
                          NOT NULL,
        status
    )
    '''
    query_works = '''
    CREATE TABLE IF NOT EXISTS Works (
        id_work INTEGER PRIMARY KEY AUTOINCREMENT
                        NOT NULL,
        work    TEXT
    )
    '''
    cursor.execute(query_employees)
    cursor.execute(query_orders)
    cursor.execute(query_statuses)
    cursor.execute(query_works)
    query_insert_employees = """ INSERT INTO Employees (id_employee,  surname) VALUES ('6', 'Иванов')"""
    query_insert_employees2 = """ INSERT INTO Employees (id_employee,  surname) VALUES ('7', 'Петров')"""
    query_insert_employees3 = """ INSERT INTO Employees (id_employee,  surname) VALUES ('8', 'Сидоров')"""
    query_insert_employees4 = """ INSERT INTO Employees (id_employee,  surname) VALUES ('9', 'Кузнецова')"""
    query_insert_employees5 = """ INSERT INTO Employees (id_employee,  surname) VALUES ('10', 'Смирнова')"""
    cursor.execute(query_insert_employees)
    cursor.execute(query_insert_employees2)
    cursor.execute(query_insert_employees3)
    cursor.execute(query_insert_employees4)
    cursor.execute(query_insert_employees5)
    query_insert_orders = ''' INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
    VALUES ('11', '16', 'Ремонт экрана смартфона', '2024-09-01', 'Иванов Игорь', '6', '1')'''
    query_insert_orders2 = ''' INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
    VALUES ('21', '16', 'Ремонт смартфона', '2024-10-06', 'Иван Петров', '6', '2')'''
    query_insert_orders3 = ''' INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
    VALUES ('22', '17', 'Замена экрана ноутбука', '2024-10-05', 'Ольга Смирнова', '6', '1')'''
    query_insert_orders4 = ''' INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
    VALUES ('23', '18', 'Установка программного обеспечения', '2024-10-04', 'Дмитрий Иванов', '7', '3')'''
    query_insert_orders5 = ''' INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
    VALUES ('24', '19', 'Чистка от пыли', '2024-10-06', 'Вадим Тришин', '8', '4')'''
    query_insert_orders6 = ''' INSERT INTO Orders (id_order, type_of_work, description, acceptance_date, customer, executor, status)
    VALUES ('25', '20', 'Замена батареи', '2024-10-06', 'Евгений Кузнецов', '6', '5')'''
    cursor.execute(query_insert_orders)
    cursor.execute(query_insert_orders2)
    cursor.execute(query_insert_orders3)
    cursor.execute(query_insert_orders4)
    cursor.execute(query_insert_orders5)
    cursor.execute(query_insert_orders6)
    query_insert_status = ''' INSERT INTO Statuses (id_status, status) VALUES ('1', 'Принят')'''
    query_insert_status2 = ''' INSERT INTO Statuses (id_status, status) VALUES ('2', 'В работе')'''
    query_insert_status3 = ''' INSERT INTO Statuses (id_status, status) VALUES ('3', 'Ожидание комплектующих')'''
    query_insert_status4 = ''' INSERT INTO Statuses (id_status, status) VALUES ('4', 'Уточнение информации')'''
    query_insert_status5 = ''' INSERT INTO Statuses (id_status, status) VALUES ('5', 'Выполнен')'''
    cursor.execute(query_insert_status)
    cursor.execute(query_insert_status2)
    cursor.execute(query_insert_status3)
    cursor.execute(query_insert_status4)
    cursor.execute(query_insert_status5)
    query_insert_works = ''' INSERT INTO Works (id_work, work) VALUES ('16', 'Ремонт смартфона')'''
    query_insert_works2 = ''' INSERT INTO Works (id_work, work) VALUES ('17', 'Замена экрана ноутбука')'''
    query_insert_works3 = ''' INSERT INTO Works (id_work, work) VALUES ('18', 'Установка программного обеспечения')'''
    query_insert_works4 = ''' INSERT INTO Works (id_work, work) VALUES ('19', 'Чистка от пыли')'''
    query_insert_works5 = ''' INSERT INTO Works (id_work, work) VALUES ('20', 'Замена батареи')'''
    cursor.execute(query_insert_works)
    cursor.execute(query_insert_works2)
    cursor.execute(query_insert_works3)
    cursor.execute(query_insert_works4)
    cursor.execute(query_insert_works5)
    query_view = '''
    CREATE VIEW IF NOT EXISTS orders_with_filter AS
    SELECT Orders.id_order,
           Works.work,
           Orders.description,
           Orders.acceptance_date,
           Orders.customer,
           Employees.surname,
           Statuses.status
      FROM Orders
           JOIN
           Works ON Orders.type_of_work = Works.id_work
           JOIN
           Employees ON Orders.executor = Employees.id_employee
           JOIN
           Statuses ON Orders.status = Statuses.id_status;
    '''
    cursor.execute(query_view)
    db.commit()
    db.close()
