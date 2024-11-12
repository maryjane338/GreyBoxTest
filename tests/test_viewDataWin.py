from PyQt6.QtWidgets import QMessageBox
from pytestqt.plugin import qtbot
from conftests import view_creation
from database.scripts.db import Data
from app.viewDataWin import ViewDataWin


def test_load_data(view_creation, qtbot):
    db = Data("..\database\\temporary_filter.db")
    win = ViewDataWin()
    win.show()
    qtbot.addWidget(win)
    win.load_data()
    assert win.table.rowCount() == 5

def test_add_data(view_creation, qtbot):
    db = Data("..\database\\temporary_filter.db")
    win = ViewDataWin()
    win.show()
    qtbot.addWidget(win)
    db.add_order(type_of_work='Ремонт', description='Ремонт описание', acceptance_date='2024-10-01',
                 customer='Федорченко Мария', executor='Иванов', status='Принят')
    db.add_order(type_of_work='Чистка', description='Чистка описание', acceptance_date='2024-10-02',
                 customer='Бредюк Матвей', executor='Иванов', status='Отклонён')
    win.load_data()
    assert win.table.rowCount() == 7

def test_remove_data(view_creation, qtbot, mocker):
    db = Data("..\database\\temporary_filter.db")
    win = ViewDataWin()
    win.show()
    qtbot.addWidget(win)
    win.table.selectRow(3)
    mocker.patch.object(QMessageBox, 'exec', return_value=QMessageBox.StandardButton.Yes)
    mocker.patch.object(QMessageBox, 'information', return_value=QMessageBox.StandardButton.Ok)
    win.del_entry.click()
    win.load_data()
    assert win.table.rowCount() == 4
