import threading,time,queue

q1 =queue.Queue(maxsize=0)  #先进先出
q1.put(1) 
q1.put(3) 
q1.put(2)

print(q1.get()) 
print(q1.get()) 
print(q1.get())

 
q = queue.PriorityQueue()

q.put((1,"moke"))
q.put((6,"she"))
q.put((3,"lol"))

print(q.get())
print(q.get())
print(q.get())



