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
        wid = QWidget()
        view_data_btn = QPushButton('Просмотреть')
        add_data_btn = QPushButton('Добавить')
        main_vl = QVBoxLayout()
        main_vl.addStretch()
        main_vl.addWidget(view_data_btn)
        main_vl.addWidget(add_data_btn)
        main_vl.addStretch()
        self.setLayout(main_vl)
        view_data_btn.clicked.connect(self.show_view_data_win)
        add_data_btn.clicked.connect(self.show_add_data_win)

    def show_view_data_win(self):
        self.win_v = ViewDataWin()
        self.win_v.show()

    def show_add_data_win(self):
        self.win_a = AddDataWin()
        self.win_a.show()

    def closeEvent(self, event):
        QApplication.quit()
