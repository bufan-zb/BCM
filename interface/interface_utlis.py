import time

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QPushButton


class BackendThread(QThread):
    update_date = pyqtSignal(dict)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit({"1":str(currentTime)})
            time.sleep(1)


class Window(QMainWindow):

    def page_setup(self):
        self.but_name_list = []
        self.but_list = []
        for i, name_list in enumerate(self.names):
            self.topwidget = QWidget()
            self.Layout.addWidget(self.topwidget)
            self.buttonLayout = QHBoxLayout(self.topwidget)
            for j, name in enumerate(name_list):
                button = QPushButton()
                button.setText(name)
                # button.resize(100, 50)
                button.setToolTip(name)
                self.buttonLayout.addWidget(button)
                self.but_list.append(button)
                self.but_name_list.append(name)