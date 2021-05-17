import json
import socket

from conf.conf import BUF_SIZE, HOST, PORT


class CacheClient():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
        self.client.connect((HOST, PORT))


    def cache_get(self, content=[]):
        """
        获取要处理的数据
        :return:字符串或者列表
        """
        if isinstance(content,str):
            content = [content]
        self.client.send(f'cache_get^&*{json.dumps(content)}'.encode())
        return json.loads(self.client.recv(BUF_SIZE).decode())

