class Person(object):
	__money = 3000
	def __init__(self,name,age):
		self.name = name 
		self.age = age 
		
	def eat(self):
		print("%s在eating"%self.name)
	
	def play(self):
		print("%s有%s"%(self.name,self.__money))
		self.__see()

	def __see(self):
		print("%s watch movie"%self.name)

m = Person("M",18)
m.play()
