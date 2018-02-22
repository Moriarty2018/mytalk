#-*- coding:utf-8 -*-

import socket
import threading



tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



def send():
    address = raw_input("请输入要连接的ip地址")
    port = raw_input("请输入端口")
    a = (address,int(port))
    tcp_socket.connect(a)
    while True:
        s = raw_input("输入消息")
        tcp_socket.send(s.encode('gb2312'))



def recv():
    i = ('',8090)
    tcp_socket.bind(i)
    while True:
        r = tcp_socket.recv(1024)
        print(r.decode("gb2312"))





def main():
    t_send = threading.Thread(target=send)
    t_recv = threading.Thread(target=recv)
    t_recv.start()
    t_send.start()
    t_recv.join()
    t_send.join()

if __name__ == "__main__":
    main()
