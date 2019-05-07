"""
该模块为数据类模块
包括：
客户类
账号类
玩家类
房间类
职业类
技能类
"""


class Client(object):
    """
    客户类，封装客户有关信息：ip，账号
    """
    def __init__(self, c_accept):
        self.io = c_accept
        self.acc = None


class Account(object):
	"""
	账号类，封装账号有关信息
	"""
    def __init__(self, id, name):
        self.acc_id = id
        self.acc_name = name
 
class Player(object):
	"""
	用于储存客户端人物层需要的数据
	"""
	def __init__(self, id, client, status, identity):
		self.id  = id
		self.client = client
		self.identity = identity		# 人物身份标识
		self.ready = False				# 表示人物是否准备
		self.life = True				# 表示人物是否存活
		self.speak = True				# 表示人物是否能够发言
 
class Room(object):
    def __init__(self, *args):
		self.id = id
        self.name = name
        self.room_master = master
        self.des = des				# 描述
        self.password = password
		self.status = status 		# 目前人数/当前人数，表示能否加入和开始游戏