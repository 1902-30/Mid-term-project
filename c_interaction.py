"""
还需要一个在游戏外（大厅·）的提示框
用于提示登录是否成功，加入房间是否成功等
"""


"""
command 所需的标识头由调用者提供
"""

from c_transfer import *
from c_control import *

ROOM_LIST = []			# 房间列表用于存放房间对象
PLAYER_LIST = []		# 玩家列表用于存放玩家对象

def log_in():
    """
    登录界面
    登录/注册界面能相互转换
    
	收集用户账号和密码
	
    return acc_id,password
    """
    pass

def register():
    """
    注册界面
    登录/注册界面能相互转换
    
	收集用户账号和密码，和第二次输入的密码
    
	return acc_id,password,again
    """
    pass
    
def hall_interface():
    """
    大厅界面
    
    需求说明：
    展现目前房间情况
    根据玩家点击进入或创建房间或刷新界面
	
	当调用的函数为create_room 或 join_room时，
	且其返回True则结束循环
	当调用refresh_room时，函数结束后需重新加载房间列表
	并进行下一轮循环
    """
    while True:# 该层循环为：当满足条件时结束该函数，否则循环进行选择
		pass
  
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
		提交信息(房间名，描述，密码（若无则空）)
		并等待接收相应结果
		需显示相应提示
	成功则 return True
    否则   return False
    """
    pass

def refresh_room():
	"""
	刷新房间
	调用submit
	获取最新的房间信息储存在ROOM_LIST中
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
	
	进入该层后首先等待服务端发送人物信息
	接收到人物信息后创建人物对象列表
	"""
    pass

def people_screen(*args, **kwargs)
	"""
	人物层
	显示人员信息（状态，身份）等
	每个人物都是独立的，减少每次更新人物信息的步骤数

	args:视情况而定各自协定
	kwargs:人员信息dict（目标位置，目标信息dict（属性：值））
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

"""
	客户端标识符
	i			acc_id
	n			acc_name
	T			操作成功
	F			操作失败
"""	
		
def main(client):
	while True:
		"""
		调用登录或注册界面
		获取用户输入
			验证注册时两次密码是否一致
				一致则下一步
				不一致则重新输入
		将用户输入传递给服务端
		并获取返回值
		根据返回值判断是否成功
			成功则将账号信息封装值client中
			失败则提示并重新循环
		"""
		pass

	# 程序正式阶段
    while True：						# 该层循环是为了保证每次游戏结束后回到大厅
        hall_interface()
		game_interface()
    
    