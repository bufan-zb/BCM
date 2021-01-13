import time

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *



from utlis import get_logger

logger = get_logger()


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)
################################################
#######创建主窗口
################################################
class FirstMainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')

        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("打开主界面")
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("打开对话框")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("打开提示框")
        self.buttonLayout.addWidget(self.pushButton3)

        names = [['7', '8', '9', '/'],
                 ['4', '5', '6', '*'],
                 ['1', '2', '3', '-'],
                 ['0', '.', '=', '+']]
        self.but_list = []
        for i, name_list in enumerate(names):
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

        # 设置中间文本
        # self.label = QLabel()
        # self.label.setText("第一个主界面")
        # self.label.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
        # self.label.setAlignment(Qt.AlignCenter)
        # self.label.setFont(QFont("Roman times", 50, QFont.Bold))
        # self.Layout.addWidget(self.label)

        # 设置状态栏
        self.statusBar().showMessage("当前用户：一心狮")

        # 窗口最大化
        self.showMaximized()

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)

        self.initUI()


    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()
        self.show()

    def handleDisplay(self, data):
        logger.info(data)
        for i in self.but_list:
            i.setText(data)

    # 按钮一：打开主界面
    windowList = []
    def on_pushButton1_clicked(self):
        the_window =SecondWindow()
        self.windowList.append(the_window)   ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window.show()


    # 按钮二：打开对话框
    def on_pushButton2_clicked(self):
        the_dialog = TestdemoDialog()
        if the_dialog.exec_() == QDialog.Accepted:
            pass



    # 按钮三：打开提示框
    def on_pushButton3_clicked(self):
        QMessageBox.information(self, "提示", "这是information框！")
        #QMessageBox.question(self, "提示", "这是question框！")
        #QMessageBox.warning(self, "提示", "这是warning框！")
        #QMessageBox.about(self, "提示", "这是about框！")





################################################
#######第二个主界面
################################################





################################################
#######对话框
################################################
class TestdemoDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('对话框')

        ### 设置对话框类型
        self.setWindowFlags(Qt.Tool)





################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_mainwindow = FirstMainWindow()
    # the_mainwindow.show()
    sys.exit(app.exec_())