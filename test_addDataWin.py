from conftests import full_db
from database.scripts.db import Data
from app.addDataWin import AddDataWin


def test_add_order(full_db, qtbot):
    db = Data("..\database\\temporary_full.db")
    win = AddDataWin()
    win.show()
    qtbot.addWidget(win)
    win.work_input.setCurrentText('Ремонт смартфона')
    win.description_input.setText('Ремонт смартфона (описание)')
    win.date_input.setText('2024-10-28')
    win.customer_input.setText('Пушкарёв Владислав')
    win.executor_input.setCurrentText('Иванов')
    win.status_input.setCurrentText('Принят')
    win.add_order()


def test_edit_data(full_db, qtbot):
    db = Data("..\database\\temporary_full.db")
    win = AddDataWin()
    win.show()
    qtbot.addWidget(win)
    real_order = {
        'id_order': 1,
        'type_of_work': 'Ремонт смартфона',
        'description': 'Ремонт смартфона (описание)',
        'acceptance_date': '2024-10-28',
        'customer': 'Пушкарёв Владислав',
        'executor': 'Иванов',
        'status': 'Принят'
    }
    win.data = list(real_order)
    win.add_order()

    real_order_edit = {
        'id_order': 1,
        'type_of_work': 'Ремонт смартфона',
        'description': 'Ремонт экрана смартфона Apple Iphone',
        'acceptance_date': '2024-10-28',
        'customer': 'Пушкарёв Владислав',
        'executor': 'Сидоров',
        'status': 'Ожидние комплектующих'
    }
    win.data = list(real_order_edit)
    win.add_order()
