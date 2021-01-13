import time

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from interface.battery_interface import Battery
from interface.engine_interface import Engine
from interface.main_interface import FirstMain



class BatteryWindow(Battery):

    def on_pushButton1_clicked(self):
        the_window = FirstMainWindow(self.x(), self.y(), self.width(), self.height())
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    def on_pushButton3_clicked(self):
        the_window = EngineWindow(self.x(), self.y(), self.width(), self.height())
        self.windowList.append(the_window)
        self.close()
        the_window.show()


class EngineWindow(Engine):

    def on_pushButton1_clicked(self):

        the_window = FirstMainWindow(self.x(), self.y(), self.width(), self.height())
        self.windowList.append(the_window)
        self.close()
        the_window.show()


    def on_pushButton2_clicked(self):
        the_window = BatteryWindow(self.x(), self.y(), self.width(), self.height())
        self.windowList.append(the_window)
        self.close()
        the_window.show()


class FirstMainWindow(FirstMain):

    def on_pushButton2_clicked(self):
        the_window =BatteryWindow(self.x(), self.y(), self.width(), self.height())
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    def on_pushButton3_clicked(self):
        the_window = EngineWindow(self.x(), self.y(), self.width(), self.height())
        self.windowList.append(the_window)
        self.close()
        the_window.show()

def start_interface():
    # 启动界面
    app = QApplication(sys.argv)
    window = QWidget()
    desktop = QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    w = 300
    h = 200
    the_mainwindow = FirstMainWindow(x, y, w, h)
    the_mainwindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_interface()