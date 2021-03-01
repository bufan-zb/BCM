import time

import multiprocessing

from conf.conf import MAIN_INTERFACE, BATERY_INTERFACE, ENGINE_INTERFACE
from interface.start_interface import start_interface
from utlis import parameter_1, save_data, parameter_0_1, car_speed, rotate_speed

data_dict = {}

para_list = MAIN_INTERFACE + BATERY_INTERFACE + ENGINE_INTERFACE

for paras in para_list:
    for key, value in paras:
        if key != "":
            data_dict[key] = "1"
data_dict["时间"] = "1"
data_dict["电压"] = "1"
data_dict["car_speed"] = 10
data_dict["rotate_speed"] = 10

if __name__ == "__main__":
    with multiprocessing.Manager() as MG:
        mydict = multiprocessing.Manager().dict(data_dict)  # 主进程与子进程共享这个字典
        myqueue = multiprocessing.Manager().Queue()

        _car_speed = multiprocessing.Process(target=car_speed, args=(mydict,))
        _rotate_speed = multiprocessing.Process(target=rotate_speed, args=(mydict,))
        _car_speed.start()
        _rotate_speed.start()

        interface = multiprocessing.Process(target=start_interface, args=(mydict,))
        data_acquisition_1 = multiprocessing.Process(target=parameter_1, args=(mydict, myqueue,))
        data_acquisition_0_1 = multiprocessing.Process(target=parameter_0_1, args=(mydict, myqueue,))
        data_save = multiprocessing.Process(target=save_data, args=(myqueue,))
        data_save.start()
        data_acquisition_1.start()
        interface.start()
        data_acquisition_0_1.start()
        interface.join()
