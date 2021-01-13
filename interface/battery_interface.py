from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from conf.conf import BATERY_INTERFACE, logger
from interface.interface_utlis import BackendThread, Window


class Battery(Window):
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
        self.names = BATERY_INTERFACE
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



    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()

    def handleDisplay(self, data):
        logger.info(data)
        for i, but in enumerate(self.but_list):
            but.setText(data.get(self.but_name_list[i], "没有数据"))
