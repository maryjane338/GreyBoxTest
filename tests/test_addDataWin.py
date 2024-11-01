from PyQt6.QtCore import Qt
from conftests import full_db
from database.scripts.db import Data
from app.addDataWin import AddDataWin
from app.viewDataWin import ViewDataWin


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
    win.add_button.click()

    db.get_all_orders(column=None, fltr=None)
    added_order = db.data[-1]
    assert added_order[1] == 'Ремонт смартфона'
    assert added_order[2] == 'Ремонт смартфона (описание)'
    assert added_order[3] == '2024-10-28'
    assert added_order[4] == 'Пушкарёв Владислав'
    assert added_order[5] == 'Иванов'
    assert added_order[6] == 'Принят'


def test_update_order(full_db, qtbot):
    db = Data("..\database\\temporary_full.db")
    win_view = ViewDataWin()
    win_view.show()
    qtbot.addWidget(win_view)

    index = win_view.table.model().index(0, 0)
    rect = win_view.table.visualRect(index)
    qtbot.mouseClick(win_view.table.viewport(), Qt.MouseButton.LeftButton, pos=rect.center())
    win = AddDataWin([win_view.table.item(win_view.table.selectedItems()[0].row(), col).text() for col in range(win_view.table.columnCount())])
    win.show()
    qtbot.addWidget(win)
    win_view.edit_entry.click()
    win.upload_editable_data()
    win.description_input.setText('Ремонт экрана смартфон Apple Iphone')
    win.customer_input.setText('Пушкарёв Владислав')
    win.executor_input.setCurrentText('Сидоров')
    win.status_input.setCurrentText('Ожидание комплектующих')
    win.add_order()

    db.get_all_orders(column=None, fltr=None)
    added_order = db.data[0]
    assert added_order[1] == 'Ремонт смартфона'
    assert added_order[2] == 'Ремонт экрана смартфон Apple Iphone'
    assert added_order[3] == '2024-09-01'
    assert added_order[4] == 'Пушкарёв Владислав'
    assert added_order[5] == 'Сидоров'
    assert added_order[6] == 'Ожидание комплектующих'


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
    win.add_button.click()

    db.get_all_orders(column=None, fltr=None)
    added_order = db.data[-1]
    assert added_order[1] == ''
    assert added_order[2] == 'Ремонт смартфона (описание)'
    assert added_order[3] == ''
    assert added_order[4] == 'Пушкарёв Владислав'
    assert added_order[5] == 'Иванов'
    assert added_order[6] == 'Принят'
