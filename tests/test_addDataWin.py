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
