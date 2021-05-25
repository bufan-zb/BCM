import json
import socket
import threading

from server.conf.conf import HOST, PORT, BUF_SIZE

def cache_get(mydict, myqueue, con):
    r = mydict.copy()
    return r

def communication(client, mydict, myqueue):
    while True:
        data = client.recv(BUF_SIZE).decode()
        if len(data)==0:
            break
        r = {}
        try:
            func, con = data.split("^&*")
            r = eval(func)(mydict, myqueue, con)
        except Exception as e:
            print(e)
            print(func)
            pass
        client.send(json.dumps(r).encode())

def connect(mydict, myqueue):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(20)  # 接收的连接数
    while True:
        client, address = server.accept()
        threading.Thread(target=communication, args=(client, mydict, myqueue)).start()
