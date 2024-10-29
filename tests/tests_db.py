import pytest
from database.scripts.db import Data
from conftests import db_creation_removal, view_creation


@pytest.mark.parametrize("type_of_work, description, acceptance_date, customer, executor, status",
                         [('Ремонт смартфона', 'Ремонт смартфона (описание)', '2024-10-28', 'Пушкарёв Владислав',
                           'Иванов', 'Принят'),
                          ('Замена экрана ноутбука', 'Замена экрана ноутбука (описание)', '2024-10-29',
                           'Мищенко Никита', 'Сидоров', 'В работе'),
                          ('Установка программного обеспечения', 'Установка программного обеспечения (описание)',
                           '2024-10-30', 'Мейдич Артемий', 'Сидоров', 'Ожидание комплектующих'),
                          ('Чистка от пыли', 'Чистка от пыли (описание)', '2024-10-31', 'Слезов Сергей', 'Петров',
                           'Уточнение информации'),
                          ('Замена батареи', 'Замена батареи (описание)', '2024-11-01', 'Дубина Степан', 'Петров',
                           'Выполнен')])
def test_add_new(db_creation_removal, type_of_work, description, acceptance_date, customer, executor, status):
    db = Data("..\database\\temporary.db")
    db.add_order(type_of_work=type_of_work, description=description, acceptance_date=acceptance_date,
                    customer=customer, executor=executor, status=status)

def test_update():
    db = Data("..\database\\temporary.db")
    db.update_order(type_of_work='Замена экрана ноутбука', description='Замена экрана ноутбука (описание)', acceptance_date='2024-10-29',
                        customer='Мищенко Никита', executor='Сидоров', status='В работе', id_order='1')

def test_removal():
    db = Data("..\database\\temporary.db")
    db.delete_order(id_order='1')

def test_get_all(view_creation):
    db = Data("..\database\\temporary_filter.db")
    db.get_all_orders(None, '2024-10-28')
