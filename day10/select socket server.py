import select,socket,queue

server = socket.socket()
server.bind(("localhost",9000))
server.listen(1000)

server.setblocking(False)#不阻塞
msg_dic = {}

inputs = [server,]
outputs = []
while True:
	readable,writeable,exceptional = select.select(inputs,outputs,inputs)
	print(readable,writeable,exceptional)
	for r in readable:
		if r is server:
			conn,addr = server.accept()
			print("来了个新连接",addr)
			inputs.append(conn)
			msg_dic[conn] = queue.Queue()
			
		else:
			data = r.recv(1024)
			print("收到数据",data)
			msg_dic[r].put(data)
			outputs.append(r)
			# r.send(data)
			# print("send done")
	for w in writeable:
		data_to_client = msg_dic[w].get()
		w.send(data_to_client)
		outputs.remove(w)
		
	for e in exceptional:
		if e in outputs:
			outputs.remove(e)
		inputs.remove(e)
		del msg_dic[e]
		
		

