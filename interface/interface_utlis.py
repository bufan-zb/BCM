import time

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QSizePolicy

from conf.conf import MAIN_INTERFACE



class SystemThread(QThread):
    para = pyqtSignal(dict)

    def __init__(self, mydict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mydict = mydict

    def system_para_update(self):
        self._para = self.mydict.copy()
        self.data_para = {
            "时间": str(QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm"))
        }



class BackendThread(SystemThread):

    def run(self):
        while True:
            self.system_para_update()
            for i in MAIN_INTERFACE:
                for key, value in i:
                    self.data_para[key] = str(self._para.get(key, "")) + value
            self.para.emit(self.data_para)
            time.sleep(1)


# class BatteryBackendThread(QThread):
#     para = pyqtSignal(dict)
#
#     def run(self):
#         while True:
#             date = QDateTime.currentDateTime()
#             currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
#             self.para.emit({"1":str(currentTime)})
#             time.sleep(1)
#
# class EngineBackendThread(QThread):
#     para = pyqtSignal(dict)
#
#     def run(self):
#         while True:
#             date = QDateTime.currentDateTime()
#             currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
#             self.para.emit({"1":str(currentTime)})
#             time.sleep(1)

class Window(QMainWindow):
    windowList = []

    def page_setup(self, title, x, y, w, h, mydict):
        self.mydict = mydict
        self.button_Adaptive = QSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setWindowTitle(title)

        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("主界面")
        self.pushButton1.setSizePolicy(self.button_Adaptive)
        self.pushButton1.setStyleSheet("border:none;")
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("电池")
        self.pushButton2.setSizePolicy(self.button_Adaptive)
        self.pushButton2.setStyleSheet("border:none;")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("发动机")
        self.pushButton3.setSizePolicy(self.button_Adaptive)
        self.pushButton3.setStyleSheet("border:none;")
        self.buttonLayout.addWidget(self.pushButton3)

        self.pushButton4 = QPushButton()
        self.pushButton4.setText("设置")
        self.pushButton4.setSizePolicy(self.button_Adaptive)
        self.pushButton4.setStyleSheet("border:none;")
        self.buttonLayout.addWidget(self.pushButton4)

        self.but_name_list = []
        self.but_list = []
        for i, name_list in enumerate(self.names):
            self.topwidget = QWidget()
            self.Layout.addWidget(self.topwidget)
            self.buttonLayout = QHBoxLayout(self.topwidget)
            for j, (name, value) in enumerate(name_list):
                if name == "":
                    continue
                button = QPushButton()
                button.setText(name)
                # button.resize(100, 50)
                button.setToolTip(name)
                button.setStyleSheet("color: black;")
                button.setSizePolicy(self.button_Adaptive)
                button.setEnabled(False)
                self.buttonLayout.addWidget(button)
                self.but_list.append(button)
                self.but_name_list.append(name)
        # 设置状态栏
        self.statusBar().showMessage("当前用户：bufan")

        self.move(x, y)
        self.resize(w, h)
        # 窗口最大化
        # self.showMaximized()

    def closeEvent(self, event):
        try:
            self.backend.terminate()
        except:
            pass
        self.close()