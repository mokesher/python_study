import time
def consumer(name):	
	print("%s 开始吃包子了"%name)
	while True:
		baozi = yield
		print("包子[%s]来了，被[%s]吃了" %(baozi,name))
def producer(name):
	c = consumer("a")             #生成器执行consumer函数
	c2 = consumer("b")            #执行2
	c.__next__()                  #生成器需要next执行下一步print
	c2.__next__()
	print("开始吃包子了")
	for i in range(10):
		time.sleep(1)
		print("做了2个包子！")
		c.send(i)
		c2.send(i)
		
producer("alex")


	
	
	
# 直接作用于for循环的对象为可迭代对象：Iterable
# 可以被next函数不断返回值对象迭代器：Iterable



'''
def fib(max):
	a,b,n = 0,1,0
	while n<max:
		yield b
		a,b = b,a+b
		n+=1
	# return "done"

a = fib(1)
try:
	print(next(a))

	print("start loop")
except StopIteration as e:
	print(e)

# for i in a:
	# print(i)
'''