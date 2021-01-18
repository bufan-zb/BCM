import time

import multiprocessing

from conf.conf import MAIN_INTERFACE, BATERY_INTERFACE, ENGINE_INTERFACE
from interface.start_interface import start_interface


data_dict = {}

para_list = MAIN_INTERFACE + BATERY_INTERFACE + ENGINE_INTERFACE

for paras in para_list:
    for key, value in paras:
        if key != "":
            data_dict[key] = 1

def func1(mydict):
    pass
    # for i in range(1000000):
    #     mydict["1"] += 1
    #     time.sleep(1)


def func2(mydict):
    pass

    # for i in range(1000000):
    #     mydict["1"] += 1
    #     time.sleep(1)


if __name__ == "__main__":
    with multiprocessing.Manager() as MG:  # 重命名
        mydict = multiprocessing.Manager().dict(data_dict)  # 主进程与子进程共享这个字典

        interface = multiprocessing.Process(target=start_interface, args=(mydict,))
        data_acquisition = multiprocessing.Process(target=func1, args=(mydict,))
        data_save = multiprocessing.Process(target=func2, args=(mydict,))
        data_acquisition.start()
        interface.start()
        data_save.start()
        interface.join()
