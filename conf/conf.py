from utlis import get_logger

MAIN_INTERFACE = [[['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                  [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                  [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                  [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]

BATERY_INTERFACE = [[['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                    [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]

ENGINE_INTERFACE = [[['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                    [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]

SETTING_INTERFACE = [[['速度', "60"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]],
                    [['速度', "KM/H"], ['电流', "A"], ['油门', "%"], ['发动机转速', "%"]],
                    [['电池剩余容量', "%"], ['剩余油量', "%"], ['最低电压', "V"], ['最高电压', "V"]]]

logger = get_logger("./root.log")
