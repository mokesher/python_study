from multiprocessing import Process,Queue

def f(q):
	q.put([1,not,"hello"])
	

if __name__ == "__main__":
	q = Queue()
	p = Process(target=f,args=(q,))
	p.start()
	print(q.get())
	p.join()
	
###复制了一份q
	
