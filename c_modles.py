class Client(object):
    """
    客户类，封装客户有关信息：ip，账号
    """
    def __init__(self, c_connect):
        self.io = c_connect
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
		# 每次游戏阶段变化后服务器将更新没人的状态，该状态将限制玩家能否发言等
		self.identity = identity	# 人物身份标识
		self.ready = False				# 表示人物是否准备
		self.life = True				# 表示人物是否存活
		self.speak = True				# 表示人物是否能够发言
		
class Room(object):
	"""
	"""
    def __init__(self, *args):
		self.id = id
        self.name = name
        self.room_master = master
        self.des = des				# 描述
		self.status = status 		# 目前人数/当前人数
		self.needpwd = needpwd      # 是否需要密码