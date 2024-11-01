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
    assert win.add_button.click() is None

    db.get_all_orders(column=None, fltr=None)
    added_order = db.data[-1]
    assert added_order[1] == 'Ремонт смартфона'
    assert added_order[2] == 'Ремонт смартфона (описание)'
    assert added_order[3] == '2024-10-28'
    assert added_order[4] == 'Пушкарёв Владислав'
    assert added_order[5] == 'Иванов'
    assert added_order[6] == 'Принят'
    

def test_invalid_data(full_db, qtbot):
    db = Data("..\database\\temporary_full.db")
    win = AddDataWin()
    win.show()
    qtbot.addWidget(win)

    win.work_input.setCurrentText('')
    win.description_input.setText('Ремонт смартфона (описание)')
    win.date_input.setText('')
    win.customer_input.setText('Пушкарёв Владислав')
    win.executor_input.setCurrentText('Иванов')
    win.status_input.setCurrentText('Принят')
    assert win.add_button.click() is None

    db.get_all_orders(column=None, fltr=None)
    added_order = db.data[-1]
    assert added_order[1] == ''
    assert added_order[2] == 'Ремонт смартфона (описание)'
    assert added_order[3] == ''
    assert added_order[4] == 'Пушкарёв Владислав'
    assert added_order[5] == 'Иванов'
    assert added_order[6] == 'Принят'
