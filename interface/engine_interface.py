from server.conf.conf import ENGINE_INTERFACE
from interface.interface_utlis import BackendThread, Window
# from server.utlis import Logger
#
# logger = Logger()

class Engine(Window):
    def __init__(self, x, y, w, h, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names = ENGINE_INTERFACE
        self.page_setup('发动机界面', x, y, w, h)

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.setEnabled(False)
        self.pushButton4.clicked.connect(self.on_pushButton4_clicked)

        self.refresh_data()


    def refresh_data(self):
        self.backend = BackendThread(self.client, self.names)
        self.backend.para.connect(self.handleDisplay)
        self.backend.start()


    def handleDisplay(self, data):
        # logger.info(data)
        self.statusBar().showMessage("当前用户：bufan;时间："+data.get("时间")[:-7])
        for i, but in enumerate(self.but_list):
            but.setText(str(data.get(self.but_name_list[i], "没有数据")))
