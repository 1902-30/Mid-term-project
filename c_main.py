from socket import *
import c_interaction as c_i
from c_modles import *
from c_setting import SERVER_ADDR


if __name__ == "__main__":
	client = socket()
	client.connect(SERVER_ADDR)
	c_i.main(Client(client))