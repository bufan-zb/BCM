from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from conf.conf import BATERY_INTERFACE
from utlis import get_logger, BackendThread

logger = get_logger()


class Battery(QMainWindow):
    windowList = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('电池界面')

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
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("电池")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("发动机")
        self.buttonLayout.addWidget(self.pushButton3)
        self.page_setup()
        # 设置状态栏
        self.statusBar().showMessage("当前用户：bufan")

        # 窗口最大化
        self.showMaximized()

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        # self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)

        self.initUI()

    def page_setup(self):
        names = BATERY_INTERFACE
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

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()

    def handleDisplay(self, data):
        logger.info(data)
        for i in self.but_list:
            i.setText(data)

    # 按钮一：打开主界面
    windowList = []

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