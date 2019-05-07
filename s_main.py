"""
该模块为
总服务程序
用于接受用户连接
创建子进程分别处理用户需求
"""


import socket
import signal
from multiprocessing import Processing, Queue
from setting import *
from modles import Client
import s_transfer as s_t
import game_main as g_m


def main():
    """
    服务端主程序入口
    """
    while True:
        client = Client(primary_server.accept()[0])
        c_processing = Processing(target=s_t.main,args=(client,game_queue))
        c_processing.start()
        client.io.close()
        del client
                

if __name__ == "__main__":
    signal.signal(signal.SIGNCHLD, signal.SIG_IGN)
     
    primary_server = socket.socket()
    primary_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    primary_server.bind(SERVER_ADDR)
    primary_server.listen(LISTEN_NUM)
    
    game_queue = Queue()
    game_server = Processing(target=g_m.main, args=(game_queue))
	game_server.start()
    
    main()