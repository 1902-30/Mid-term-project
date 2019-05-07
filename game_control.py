"""
该模块为游戏内逻辑


游戏内逻辑要求：
夜晚时即使相应角色已全部死亡，仍需进行其回合
女巫毒人/救人流程时间10s
狼人刀人流程时间30s		不能发言，当平票时有一次重投的机会（每个流程仅一次）
"""	


def day_process():
	"""
	白天流程
	"""
	pass

def speech():
	"""
	白天轮次发言过程
	"""
	pass
	

def night_process():
	"""
	夜晚流程
	"""
	pass
	
def kill():
	"""
	狼人刀人流程
	"""
	pass

def poison()
	"""
	女巫毒人流程
	"""
	pass

def resscue():
	"""
	女巫救人流程
	"""
	pass

def vote_process();
	"""
	投票流程
	"""
	pass
	
def game_judge():
	"""
	游戏是否结束的判定
	可能造成游戏结束的流程结束后调用此函数进行判断
	若结束return：True
	否则  return：False
	"""
	pass
	
def settle(*args, **kwargs):
	"""
	游戏结算
	向所有玩家回发游戏结算数据
	并写入数据库
	
	args:视情况而定
	kwargs:视情况而定
	"""
	pass