import multiprocessing
import time
import json





para = {
    "电池电压": ["电压1", "电压2", "电压3", "电压4", "..."],
    "发动机点火": {"时间戳秒级": 1},
    "温度": [],
    "电机霍尔": {"时间戳秒级": 1},
    "电流": 2.2,
    "发动机转速限制": 2,
    "电动车速限制": 1,
    "把手霍尔电压": 3,
    "限制霍尔电压": 4,
    "": [],
    "": [],
    "": [],
    "": [],
    "": [],
    "": [],
    "": [],
}



def func(mydict):
    for i in range(1000000):
        mydict["s"]+=1


if __name__ == "__main__":
    with multiprocessing.Manager() as MG:  # 重命名
        mydict = multiprocessing.Manager().dict({"s":0})  # 主进程与子进程共享这个字典

        p = multiprocessing.Process(target=func, args=(mydict,))
        a = multiprocessing.Process(target=func, args=(mydict,))
        p.start()
        a.start()
        # p.join()
        while True:
            time.sleep(1)
            r = mydict.copy()
            print(json.dumps(r))
            # print(dir(mydict))
            print(mydict)