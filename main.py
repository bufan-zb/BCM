import threading

import time

import multiprocessing

from conf.conf import MAIN_INTERFACE, BATERY_INTERFACE, ENGINE_INTERFACE
from interface.start_interface import start_interface
from utlis import rotate_speed, car_speed, parameter_1, parameter_0_1, save_data

data_dict = {}

para_list = MAIN_INTERFACE + BATERY_INTERFACE + ENGINE_INTERFACE

for paras in para_list:
    for key, value in paras:
        if key != "":
            data_dict[key] = "1"
data_dict["时间"] = "1"
data_dict["电压"] = "1"
data_dict["state"] = True

def high(mydict, myqueue):
    _rotate_speed = threading.Thread(target=rotate_speed, args=(mydict,))
    _car_speed = threading.Thread(target=car_speed, args=(mydict,))
    _rotate_speed.start()
    _car_speed.start()
    _rotate_speed.join()
    _car_speed.join()

def middle(mydict, myqueue):
    data_acquisition_1 = threading.Thread(target=parameter_1, args=(mydict, myqueue,))
    data_acquisition_0_1 = threading.Thread(target=parameter_0_1, args=(mydict, myqueue,))
    data_acquisition_1.start()
    data_acquisition_0_1.start()
    # 启动界面
    start_interface(mydict, myqueue)

def low(mydict, myqueue):
    data_save = threading.Thread(target=save_data, args=(myqueue,))
    data_save.start()


if __name__ == "__main__":
    with multiprocessing.Manager() as MG:
        mydict = multiprocessing.Manager().dict(data_dict)  # 主进程与子进程共享这个字典
        myqueue = multiprocessing.Manager().Queue()
        # 优先级高进程(实时性要求高；如:发动机转速，电机转速....)
        _high = multiprocessing.Process(target=high, args=(mydict, myqueue))
        _high.start()
        # 优先级中进程(实时性要求一般；如:界面显示....)
        _middle = multiprocessing.Process(target=middle, args=(mydict, myqueue))
        _middle.start()
        # 优先级低进程(实时性要求低；文件存储，离线任务.....)
        _low = multiprocessing.Process(target=low, args=(mydict, myqueue))
        _low.start()

        while mydict["state"]:
            time.sleep(1)
