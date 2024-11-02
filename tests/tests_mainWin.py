from pytestqt.plugin import qtbot
from conftests import full_db
from app.mainWin import MainWin
from database.scripts.db import Data


def test_button_interaction_view_data(full_db, qtbot):
    db = Data("..\database\\temporary_full.db")
    win = MainWin()
    win.show()
    qtbot.addWidget(win)
    assert win.view_data_btn.click() is None


def test_button_interaction_add_data(full_db, qtbot):
    db = Data("..\database\\temporary_full.db")
    win = MainWin()
    win.show()
    qtbot.addWidget(win)
    assert win.add_data_btn.click() is None
