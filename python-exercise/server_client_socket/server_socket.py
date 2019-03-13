#!/usr/bin/env python

import socket
import threading
import time

def tcplink(sock,addr):
    print("Accept new connection from %s: %s...." % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode("utf-8") == "exit":
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print("Connection from %s: %s closed" % addr)

#创建socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 先组队IP地址和端口，然后监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)
print("Waiting for connection...")

#通过永久循环来接收来自客户端的连接
while True:
    sock, addr = s.accept() #接受一个新连接
    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock,addr))
    t.start()
