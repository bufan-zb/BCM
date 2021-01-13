import time

import logging
from PyQt5.QtCore import QThread, pyqtSignal, QDateTime


def get_logger():
    logging.basicConfig(
        filename="root.log",
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%m/%d %H:%M:%S'
    )
    logger = logging.getLogger(__name__)
    return logger


class BackendThread(QThread):
    update_date = pyqtSignal(str)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit(str(currentTime))
            time.sleep(1)