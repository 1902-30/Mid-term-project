"""
一些通用功能
"""

import mysql
from setting import *


def conn_databases():
	"""
	连接数据库
	"""
	pass

def sql_wr(sql, *args, **kwargs):
    """
	执行数据库读 or 写操作
    获取影响的行和相应的读或写的数据
	
	sql:需执行的语句
	args:视情况而定各自协定
	kwargs:视情况而定各自协定
	
	return:tuple(影响的行,查找到的内容)
    """
    pass
	
def data_split():
	"""
	用于收到的消息预处理
	将其拆分为标识头和字典并返回
	"""
	pass
	

def data_joint():
	"""
	发送消息前
	通过该函数将信息（标识头+字典）
	处理成标准格式
	"""
	pass
    
def send_info(target, data):
	"""
    data:       信息内容
	在适当的时候传回适当的数据
	"""
	pass

def screening_out(data):
	"""
	检测屏蔽词
	屏蔽词词库储存在文本中
	
	data:需检查的内容
	
	若
	存在则	return:处理后的文本
	否则	return:None
	"""
	pass
	
def blank_check():
	"""
	检测空格
	"""
	pass