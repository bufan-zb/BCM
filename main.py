import time

import sys
from PyQt5.QtWidgets import QApplication


from interface.battery_interface import Battery
from interface.engine_interface import Engine
from interface.main_interface import FirstMain
from utlis import get_logger

logger = get_logger()


class BatteryWindow(Battery):


    def on_pushButton1_clicked(self):
        the_window = FirstMainWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    # 按钮三：打开提示框
    def on_pushButton3_clicked(self):
        the_window = EngineWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()


class EngineWindow(Engine):

    def on_pushButton1_clicked(self):
        the_window = FirstMainWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()


    def on_pushButton2_clicked(self):
        the_window = BatteryWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()


class FirstMainWindow(FirstMain):

    def on_pushButton2_clicked(self):
        the_window =BatteryWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()

    def on_pushButton3_clicked(self):
        the_window = EngineWindow()
        self.windowList.append(the_window)
        self.close()
        the_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = FirstMainWindow()
    the_mainwindow.show()
    sys.exit(app.exec_())