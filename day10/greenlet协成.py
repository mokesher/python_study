from greenlet import greenlet

def test1():
	print(11)
	gr2.switch()
	print(22)
	gr2.switch()

def test2():
	print(23)
	gr1.switch()
	print(77)

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
