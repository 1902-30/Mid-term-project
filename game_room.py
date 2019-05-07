"""
游戏内房间模块
用于收发聊天信息和游戏流程控制
用户进入房间后对客户端的消息收发由本进程控制

io复用或协程
协程是否可监听queue？
"""

"""
可能导入和定义全局变量需要放到main中去
"""


from select import *
from common import *
from s_modles import *
import game_control as g_c
import s_transfer.send_info as send_info


PLAYERS_LIST = []
WOLF_LIST = []
PEOPLE_LIST = []
PROPHET_LIST = []
WITCH_LIST = []
HUNTER_LIST = []
DICT_IO = {}


def update_status():
	"""
	用于告知客户端其状态已更新
	"""
	pass

def join_room():
	"""
	玩家加入房间
	"""
	data = room_pipe.recv()
	PEOPLE_LIST.append(Player(data[0], 0, None))
	ep.register(data[0].io.fileno(), EPOOLIN)
	DICT_IO[data[0].io.fileno()] = data[0]
	data[1].put("True")
	sql_wr(sql)		# 更新房间信息（房间人数信息）
	send_info(data[0].io,"T 加入房间成功")
	"""
	将目前房间内玩家的信息发送给客户
	"""
	pass
	

def client_input():
	"""
    1
	调用send_info
    将用户的输入发送给房间其他玩家
	"""
    pass

def client_voice():
    """
    2
	调用send_info
    将用户的语音发送给房间内其他玩家
    """
    pass

def ready_go():
	"""
	3
	修改用户准备状态
	并告知其他用户
	"""
    pass

def game_start():
	"""
	5
	游戏开始
	首先需要判断是不是房主
	"""
	pass	

def select():
    """
    8
	处理用户技能方面的选择
	每当用户选择后发送信息给其他用户
	并记下当前最高票
    """
	pass

def client_exit(client):
	"""
	用户退出处理
	
	client：用户对象
	群发消息，移除列表
	"""
	pass

def recv(client)
    """
    游戏内接收函数
	接收信息并调用响应函数
    协议：			使用英文单词前三个字母（首字母大写）   
	1.Inp			消息：群发
	2.Voi			语音：群发
	3.Rea			人员准备：群发
	4.Sta			游戏开始：群发
	5.Sel			技能等选择
	6.Exi			退出：群发
	"""
    pass

def before_starting():
	"""
	接收新加入的人员
	和内部人员的消息
	"""
	ep = epoll()
	ep.register(room_pipe.fileno(), EPOOLIN)
	while True:
		events = ep.epool()
		for fd,event in events:
			if fd == room_pipe.fileno():
				join_room()
			else:
				data = recv(DICT_IO[fd])
				if data == "start":
					break

def role_assignment():
	"""
	角色分配
	"""
	pass
				
def game_start():
	while True:
		break if g_c.day_process()
		break if g_c.night_process()

	
def main(room_pipe, WAIT_ROOM_DICT):
	before_starting()
	role_assignment()
	game_start()