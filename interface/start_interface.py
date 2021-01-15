import time

import sys
from PyQt5.QtWidgets import QApplication, QWidget

from interface.battery_interface import Battery
from interface.engine_interface import Engine
from interface.main_interface import FirstMain
from interface.setting_interface import Setting


def pushButton1(self):
    the_window = FirstMainWindow(self.x(), self.y(), self.width(), self.height(), self.mydict)
    the_window.mydict = self.mydict
    self.windowList.append(the_window)
    if self.backend != None:
        self.backend.terminate()
    self.close()
    del self.windowList[0]
    the_window.show()

def pushButton2(self):
    the_window = BatteryWindow(self.x(), self.y(), self.width(), self.height(), self.mydict)
    the_window.mydict = self.mydict
    self.windowList.append(the_window)
    if self.backend != None:
        self.backend.terminate()
    self.close()
    del self.windowList[0]
    the_window.show()

def pushButton3(self):
    the_window = EngineWindow(self.x(), self.y(), self.width(), self.height(), self.mydict)
    the_window.mydict = self.mydict
    self.windowList.append(the_window)
    if self.backend != None:
        self.backend.terminate()
    self.close()
    del self.windowList[0]
    the_window.show()


def pushButton4(self):
    the_window = SettingWindow(self.x(), self.y(), self.width(), self.height(), self.mydict)
    the_window.mydict = self.mydict
    self.windowList.append(the_window)
    if self.backend != None:
        self.backend.terminate()
    self.close()
    del self.windowList[0]
    the_window.show()



class BatteryWindow(Battery):

    def on_pushButton1_clicked(self):
        pushButton1(self)

    def on_pushButton3_clicked(self):
        pushButton3(self)

    def on_pushButton4_clicked(self):
        pushButton4(self)

class SettingWindow(Setting):

    def on_pushButton1_clicked(self):
        pushButton1(self)

    def on_pushButton2_clicked(self):
        pushButton2(self)

    def on_pushButton3_clicked(self):
        pushButton3(self)


class EngineWindow(Engine):

    def on_pushButton1_clicked(self):
        pushButton1(self)


    def on_pushButton2_clicked(self):
        pushButton2(self)


    def on_pushButton4_clicked(self):
        pushButton4(self)


class FirstMainWindow(FirstMain):

    def on_pushButton2_clicked(self):
        pushButton2(self)

    def on_pushButton3_clicked(self):
        pushButton3(self)

    def on_pushButton4_clicked(self):
        pushButton4(self)

def start_interface(mydict):
    # 启动界面
    app = QApplication(sys.argv)
    window = QWidget()
    desktop = QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    w = 300
    h = 200
    the_mainwindow = FirstMainWindow(x, y, w, h, mydict)
    the_mainwindow.windowList.append(the_mainwindow)
    the_mainwindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_interface()