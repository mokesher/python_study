import socket

HOST = "localhost"
POST = 9000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,POST))
while True:
	msg = bytes(input(">>:"),encoding="utf-8")
	s.sendall(msg)
	# data = s.recv(1024)
	# print(data)
	# print("Recevied:",repr(data))
	
s.close()