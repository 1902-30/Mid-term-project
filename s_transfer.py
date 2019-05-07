"""
该模块为服务器与客户端交互模块
进行简单处理后交由服务器逻辑模块处理
并返回处理结果给客户端
"""

"""
用户的每一次状态改变都需要记录相应的日志到数据库
	登录登出日志
	游戏内对局日志

用户注册，创建房间文字等都需经过屏蔽检测处理，若
"""


from os import _exit
from select import select
from multiprocessing import Queue
from modles import *
from common import *
import server_control as s_c
import game_control as g_c


def log_wrap():
	"""
	日志操作用装饰器
	
	暂时无视，
	根据后续情况决定是否使用该装饰器
	"""
	pass
	
def recv_wrap():
	"""
	消息接收类函数用装饰器
	
	请无视：这是最后优化时的工作
	判断是否为用户退出消息(正常和异常)
	
	将接收到的信息解析为标识头+键值对
	
	备注：用户退出后需修改数据库中用户status值
	"""
	pass

def log_in(**kwargs):
	"""
	0
	调用s_c.log_in
	
	kwargs:用户提供的信息
	
	并返回其返回值
	"""
	pass

def register(**kwargs):
	"""
	1
	调用s_c.register
	
	kwargs:用户提供的信息
	
	并返回其返回值
	"""
	pass

def join_room(room_id, password=None, *args, **kwargs):
    """
    2
	整理传入数据
    并调用s_c.join_room
	
    room_id:房间号
    password:房间密码
    args:视情况而定
	kwargs:视情况而定
    
	成功则:
		return 函数结果
	否则:
		调用send_info返回结果给客户端
		return None
    """
	pass

def create_room(*args, **kwargs):
    """
    3
    整理传入数据
    并调用s_c.create_room
	
    args:视情况而定
    kwargs:房间信息
	
	成功则:
		return 函数结果
	否则:
		调用send_info返回结果给客户端
		return None
    """
    pass

def refresh_room():
	"""
    4
    调用s_c.refresh_room
	接收新的房间信息
	并发送给客户端
	
	return None
	"""
	pass

def log_recv():
	"""
	登录部分用接收函数
	协议：			使用英文单词前三个字母（首字母大写）
	0.Log			登录
	1.Reg			注册
	根据协议调用相应函数
	
	return 函数结果（tuple(id, name)）
	"""
	pass

def join_room_recv():
	"""
	进入房间部分接收函数
	协议：			使用英文单词前三个字母（首字母大写）
	2.Joi			进入房间
	3.Cre			创建房间
	4.Reg			刷新大厅界面
	根据协议调用相应函数
	
	return 函数结果（）
	"""
	pass

def main(client, game_queue):
	while True:
	# 接收用户登录信息，成功登录则退出当前循环
		acc_info = log_recv()
		break if acc_info is not None
	# 储存用户账号信息
	client.acc = Account(*acc_info)
	# 创建与房间进程通信用消息队列
	queue = Queue()
    while True:
	# 使客户循环的进行游戏
		while True:
		# 加入、创建、刷新房间
			operation = join_room_recv()
			break if operation is not None
		method, room_id = operation
		game_queue.put((method, room_id, client, queue)) 
		try:
			msg = queue.get(timeout=3)
		except:
			send_info(client.io, "F 服务器拥挤")
		if msg == "False":
			send_info(client.io, "F 房间不存在")
			break
		queue.get()