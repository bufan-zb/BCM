from conf.conf import MAIN_INTERFACE, logger
from interface.interface_utlis import BackendThread, Window


class FirstMain(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.names = MAIN_INTERFACE
        self.page_setup('主界面')


        ###### 三个按钮事件 ######
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
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