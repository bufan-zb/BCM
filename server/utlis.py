import datetime
import os

import json

import time
import pandas as pd

from conf.conf import ONE_COL_NAME, LOG_PATH
from conf.conf import TEST


class Logger(object):
    """日志按日期写入文件"""
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            obj = object.__new__(cls, *args, **kwargs)
            cls.__instance = obj
            return cls.__instance

    def __init__(self):
        self.path = LOG_PATH

    def info(self, msg):
        file_path = self.path + "/{}.log".format(time.strftime('%Y-%m-%d'))
        msg = "{}   ".format(time.strftime('%Y-%m-%d %H:%M:%S')) + str(msg) + "\n"
        if TEST:
            print(msg, end="")
        with open(file_path, "a+") as f:
            f.write(msg)

    def __call__(self, msg, *args, **kwargs):
        self.info(msg)

logger = Logger()

class PandasWriteR():
    """pandas追加写入"""
    __instance = None
    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        else:
            obj = object.__new__(cls, *args, **kwargs)
            cls.__instance = obj
            return cls.__instance

    def __init__(self):
        self.path = "databases"
        self.current_path = self.path + "/{}".format(time.strftime('%Y-%m-%d')) +"/{}.csv"
        self.file_path = ""
        self.file_col_name_list = ONE_COL_NAME

    def write(self, df, filename):
        file_path = self.path + "/{}/{}.csv".format(time.strftime('%Y-%m-%d'), filename)
        df = df[self.file_col_name_list[filename]]
        # 判断当前日期目录是否存在
        if not os.path.isdir(self.path + "/{}".format(time.strftime('%Y-%m-%d'))):
            os.mkdir(self.path + "/{}".format(time.strftime('%Y-%m-%d')))
        # 判断文件是否存在，是否写入表头
        header = True
        if os.path.isfile(file_path):
            header = False
        df.to_csv(file_path, mode='a', header=header, index=False)


def parameter_1(mydict, myqueue):
    # 每秒钟获取一次的参数
    while True:
        mydict["时间"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logger.info(mydict)
        myqueue.put_nowait({"json": dict(mydict.copy()), "file_name": ["电动车速度", "发动机转速", "电流", "电压", "油门"]})
        time.sleep(1)


def parameter_0_1(mydict, myqueue):
    # 每0.1秒钟获取一次的参数
    while True:
        time.sleep(0.1)


def save_data(myqueue):
    # 把数据保存到对应的文件中
    write = PandasWriteR()
    while True:
        data = myqueue.get()
        df = pd.DataFrame(data["json"], index=[0])
        for i in data["file_name"]:
            write.write(df, i)

def rotate_speed(mydict):
    t1 = str(int(time.time()))
    speed_list = []
    while True:
        time.sleep(0.1)
        t = str(int(time.time()))
        if t1 != t:
            t1 = t
            mydict["发动机转速"] = len(speed_list)*60
            speed_list = []
        speed_list.append(1)

def car_speed(mydict):
    t1 = str(int(time.time()))
    speed_list = []
    while True:
        time.sleep(0.1)
        t = str(int(time.time()))
        if t1 != t:
            t1 = t
            mydict["速度"] = len(speed_list)*50
            speed_list = []
        speed_list.append(1)

def merge_one_day_data():
    pass

if __name__ == '__main__':
    # 测试日志写入
    logger = Logger()
    logger.info("nihao")
    # 测试pandas写入
    data = {"json":pd.DataFrame({"id": 1, "name": "zoubin", "age": 18}, index=[0]).to_json(),
            "file_name": ["test"]}
    write = PandasWriteR()
    write.file_col_name_list = {"test": ["id", "name", "age"]}
    df = pd.DataFrame(json.loads(data["json"]))
    write.write(df, "test")
