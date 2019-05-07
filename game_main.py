"""
该模块为
接收加入房间的信息
创建游戏房间子进程

优化：使Pipe能够复用来达到优化的目的
"""

from multiprocessing import Process, Pipe, Manager
import game_room as g_r

WAIT_ROOM_DICT = Manager().dict() # {"id":Queue()}
RUN_ROOM_DICT = Manager().dict()	# {"id":Queue()}		不一定要用，后期再扩展


def main(game_queue):
	while True:
		data = game_queue.get()		# (method(join，create), room_id, client, queue)
		if data[0] == "join":
			try:
				WAIT_ROOM_DICT[data[1]].send((data[2], data[3]))
			except KeyError:
				data[3].put("False")
		elif data[0] == "create":
			room_pipe = Pipe()
			room = Process(target=g_r.main, args=(room_pipe[1],WAIT_ROOM_DICT))
			WAIT_ROOM_DICT[data[1]] = room_pipe[0]
			WAIT_ROOM_DICT[data[1]].send((data[2], data[3]))
			room.start()
			del room_queue
			del room
			
			
			
		