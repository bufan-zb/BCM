from PyQt5.QtWidgets import QSizePolicy, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit

from conf.conf import SETTING_INTERFACE
from interface.interface_utlis import BackendThread, Window
from utlis import Logger

logger = Logger()

class Setting(Window):
    def __init__(self, x, y, w, h, mydict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names = SETTING_INTERFACE
        self.page_setup('设置', x, y, w, h, mydict)

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton4.setEnabled(False)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)
        self.backend = None

        # self.refresh_data(mydict)


    def refresh_data(self, mydict):
        self.backend = BackendThread(mydict, self.names)
        self.backend.para.connect(self.handleDisplay)
        self.backend.start()


    def handleDisplay(self, data):
        logger.info(data)
        self.statusBar().showMessage("当前用户：bufan;时间："+data.get("时间")[:-7])
        for i, but in enumerate(self.but_list):
            but.setText(str(data.get(self.but_name_list[i], "没有数据")))

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
                label = QLabel()
                label.setText(name)
                label.setSizePolicy(self.button_Adaptive)
                self.buttonLayout.addWidget(label)
                text = QLineEdit()
                text.setText(str(value))
                text.setSizePolicy(self.button_Adaptive)
                self.buttonLayout.addWidget(text)
                self.but_list.append(text)
                self.but_name_list.append(name)

        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)
        self.submitButton = QPushButton()
        self.submitButton.setText("提交")
        # button.resize(100, 50)
        # button.setToolTip(name)
        self.submitButton.setStyleSheet("color: black;")
        self.submitButton.setSizePolicy(self.button_Adaptive)
        self.submitButton.clicked.connect(self.on_submitButton_clicked)
        # button.setEnabled(False)
        self.buttonLayout.addWidget(self.submitButton)
        # 设置状态栏
        self.statusBar().showMessage("当前用户：bufan")

        self.move(x, y)
        self.resize(w, h)
        # 窗口最大化
        # self.showMaximized()

    def on_submitButton_clicked(self):
        logger.info("点击提交")
