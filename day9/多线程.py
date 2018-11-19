import threading,time

def run(n):
	print("task:",n)
	time.sleep(2)
	print("task done",threading.current_thread())

# t1 = threading.Thread(target=run,args=("t1",))
# t2 = threading.Thread(target=run,args=("t2",))
# t1.start()
# t2.start()	

start_time = time.time()
t_obj = []
for i in range(50):
	t = threading.Thread(target=run,args=("t-%s"%i,))
	t.setDaemon(True)		#当前线程设为主线程 守护进程
	t.start()
	t_obj.append(t)

# for t in t_obj:
	# t.join()
print("------all threads has finished..")
print("cost:",time.time()-start_time)
