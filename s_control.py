"""
服务器逻辑模块
用于处理服务端与客户端交互模块传入的数据，并返回结果

用户账号使用自增数
房间号使用日期+时间+游戏编号+#+用户id
房间信息储存在数据库中
"""


from models import *
from common import *


def log_wrap():
	"""
	日志操作装饰器
	暂时无视，
	根据后续情况决定是否使用装饰器
	"""
	pass

def log_in(**kwargs):
    """
    0
	用户登录
	
	kwargs:用户提供的信息
	
	验证用户登录信息
	调用sql_wr()  传入参数：sql
		若登录失败：
			send_info(client.io,"F 登录失败")
			return None
		若登录成功：
			需从数据库提取用户名，并修改数据库中用户status值
			调用sql_wr()  传入参数：sql
			send_info(client.io,msg)    msg 为id，name的键值对
			return tuple(id, name)
		
	
	
    """
    pass

def register(**kwargs):
	"""
    1
	新用户注册
	
	kwargs:用户提供的信息
	
	验证用户名是否符合要求
	屏蔽字检测，不许有空格
		若未通过：
			send_info(client.io,"F 注册失败，失败原因")
			return None
		通过：
			注册新用户，将用户信息写入数据库
			调用sql_wr()  传入参数：sql，
			sql中需包含status信息
			send_info(client.io,msg)    msg 为id，name的键值对
			return tuple(id, name)
	"""
	pass

def join_room(acc_no, *args, **kwargs):
    """
    根据获得信息进行信息比对
	判断是否能加入房间
	
	acc_no:账号
	args:视情况而定各自协定
	kwargs:密码等信息
	
    是则 return join, room_id
    否则 return 相应信息
    """
    pass
	
def create_room(acc_no, *args, **kwargs):
    """
    比对当前信息（屏蔽字）
	判断是否能创建房间
	
	acc_no:账号
	args:视情况而定各自协定
	kwargs:房间信息
	
    是则调用sql_wr创建房间
		并return create, room_id
    否则  return 相应信息
    """
    pass

def refresh_room(*args, **kwargs):
    """
	调用sql_wr获取最新的房间信息
    返回最新的房间信息
	不返回密码仅返回是否有密码
	
	args:视情况而定各自协定
	kwargs:视情况而定各自协定
	
	return 房间信息
    """
    pass

