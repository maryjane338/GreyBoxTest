from pytestqt.plugin import qtbot
from conftests import db_creation_removal
from app.mainWin import MainWin
from database.scripts.db import Data


def test_button_interaction_view_data(db_creation_removal, qtbot):
    db = Data("..\database\\temporary.db")
    win = MainWin()
    win.show()
    qtbot.addWidget(win)
    assert win.view_data_btn.click

def test_button_interaction_add_data(db_creation_removal, qtbot):
    db = Data("..\database\\temporary.db")
    win = MainWin()
    win.show()
    qtbot.addWidget(win)
    assert win.add_data_btn.click
