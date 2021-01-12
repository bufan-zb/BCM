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
    for i in range(100000):
        mydict["s"]+=1

mydict = multiprocessing.Manager().dict({"s":0})  # 主进程与子进程共享这个字典
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# # 电池电压
# battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])

#	实时车速
real_time_speed = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	最大车速
max_speed = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	实时电流
electricity = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	油门
accelerator = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	发动机转速r/min
rotate_speed = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	剩余电量
remaining_soc = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	剩余油量
remaining_oil = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	最大电压电池
max_battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
#	最小电压电池
min_battery_voltage = multiprocessing.Manager().list(["电压1", "电压2", "电压3", "电压4", "..."])
# 电池进程
p = multiprocessing.Process(target=func, args=(mydict,))
# 发动机进程
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