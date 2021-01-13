from conf.conf import BATERY_INTERFACE, logger
from interface.interface_utlis import BackendThread, Window


class Battery(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names = BATERY_INTERFACE
        self.page_setup('电池界面')

        ###### 三个按钮事件 ######
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton3.clicked.connect(self.on_pushButton3_clicked)

        self.refresh_data()



    def refresh_data(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.backend.start()

    def handleDisplay(self, data):
        logger.info(data)
        for i, but in enumerate(self.but_list):
            but.setText(data.get(self.but_name_list[i], "没有数据"))
