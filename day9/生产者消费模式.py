import threading,time,queue

q = queue.Queue(maxsize=10)

def Producer(name):
	count = 1
	while True:
		q.put("骨头%s"%count)
		print("生产了%s骨头"%count)
		count +=1
		time.sleep(0.5)
		
def Consumer(name):
	while True:
		print("[%s] 取到[%s] 并吃到了..."%(name,q.get()))
		time.sleep(1)
		
p = threading.Thread(target=Producer,args=("alex",))
c = threading.Thread(target=Consumer,args=("mmm",))

p.start()
c.start()

		