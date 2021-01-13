from conf.conf import ENGINE_INTERFACE, logger
from interface.interface_utlis import BackendThread, Window


class Engine(Window):
    def __init__(self, x, y, w, h, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names = ENGINE_INTERFACE
        self.page_setup('发动机界面', x, y, w, h)

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        self.pushButton3.setEnabled(False)

        self.refresh_data()


    def refresh_data(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()


    def handleDisplay(self, data):
        logger.info(data)
        for i, but in enumerate(self.but_list):
            but.setText(data.get(self.but_name_list[i], "没有数据"))
