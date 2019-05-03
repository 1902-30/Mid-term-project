"""
还需要一个在游戏外（大厅·）的提示框
"""


"""
command 所需的标识头由调用者提供
"""
import c_control as c_c
from select import select

ROOM_LIST = []

def log_in():
    """
    登录界面
    登录/注册界面能相互转换，有退出按钮
    
	收集用户账号和密码
	使用command发送
    recv接收回执信息
	
    登录成功:return:tuple(用户ID，用户名)
	登录失败:return None
    """
    pass

def register():
    """
    注册界面
    登录/注册界面能相互转换，有退出按钮
    
	收集用户账号和密码
	使用command发送
    recv接收回执信息
    
    注册成功:return:tuple(用户ID，用户名)
	注册失败:return None
    """
    pass
    
def hall_interface():
    """
    大厅界面
    
    需求说明：
    展现目前房间情况
    根据玩家点击进入或创建房间或刷新界面
    """
    while True:						# 该层循环为：当满足条件时结束该函数，否则循环进行选择
		pass                        # 当调用的函数为create_room 或 join_room时，且其返回True(使用 is True 判断)则结束循环
  
def join_room():
    """
    加入房间界面
    展示房间信息
    如果有需要输入密码
    调用command、recv
		提交信息(room_id，密码（若无则空）)
		并等待接收相应结果
		需显示相应提示
    成功则 return True
    否则   return False
    """

def create_room():
    """
    创建房间界面
    获取用户输入的房间名等信息
    调用command、recv
	提交信息
    并等待接收相应结果
    """
    pass
    
def game_interface():
    """
    游戏内界面
	初步分为三层：
		第一层：人物层，显示人员信息（状态，身份）等
		第二层：会话层，显示当前阶段（背景图片显示）及人物发言等
		第三层：输入层，用于获取用户输入信息（文字和语音）等
	整合三层拼接到一起
	"""
    pass

def people_screen(target, info, *args, **kwargs)
	"""
	人物层
	显示人员信息（状态，身份）等
	每个人物都是独立的，减少每次更新人物信息的步骤数
	
	target:需更改的目标
	info::新的信息		dict(属性：值)
	args:视情况而定各自协定
	kwargs:视情况而定各自协定
	"""
	pass

def conversation_screen(data, *args, **kwargs):
	"""
	会话层
	获取recv接收到的数据
	显示当前阶段（背景图片显示）及人物发言
	
	data:（dict：{消息源：消息内容}）
	args:视情况而定各自协定
	kwargs:视情况而定各自协定
	"""
	pass
	
def input_screen():
	"""
	输入层
	收集用户输入信息
	包括语音和文本
	使用command发送
	
	要求
	当用户处于暂时不能发言却点击发送的情况时
	已键入的文本不会被清除
	
	处于不能发言的情况时语音按钮点击无效
	"""
	pass

def command(iden, data, *args, **kwargs):
	"""
	发送端
	向服务端发送用户指令
	
	iden:标识头（见s_transfer.py）
	data:内容
	args:视情况而定各自协定
	kwargs:视情况而定各自协定
	"""
	pass

def recv(iden, data, *args, **kwargs):
	"""
	接收端
	根据服务器返回的数据调用响应的函数，
	展示效果（变化）
	
	iden:标识头（未定）
	data:内容
	args:视情况而定各自协定
	kwargs:视情况而定各自协定
	"""

def main(client):
	while True:
        acc = log_in()
        break if acc is not None
	client.acc = Account(*acc)
    while True：						# 该层循环是为了保证每次游戏结束后回到大厅
        hall_interface()
		game_interface()
    
    