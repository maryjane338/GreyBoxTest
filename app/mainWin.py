from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication
from PyQt6.QtGui import QIcon
from app.addDataWin import AddDataWin
from app.viewDataWin import ViewDataWin


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Сервисный центр')
        self.resize(300, 400)
        self.setFixedSize(self.width(), self.height())
        self.setWindowIcon(QIcon('resources/computer.ico'))
        self.view_data_btn = QPushButton('Просмотреть')
        self.add_data_btn = QPushButton('Добавить')
        self.main_vl = QVBoxLayout()
        self.main_vl.addStretch()
        self.main_vl.addWidget(self.view_data_btn)
        self.main_vl.addWidget(self.add_data_btn)
        self.main_vl.addStretch()
        self.setLayout(self.main_vl)
        self.view_data_btn.clicked.connect(self.show_view_data_win)
        self.add_data_btn.clicked.connect(self.show_add_data_win)

    def show_view_data_win(self):
        self.win_v = ViewDataWin()
        self.win_v.show()

    def show_add_data_win(self):
        self.win_a = AddDataWin()
        self.win_a.show()

    def closeEvent(self, event):
        QApplication.quit()
