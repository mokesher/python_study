class People(object):
	def __init__(self,name,age):
		self.name = name
		self.age  =age

	def eat(self):
		print("%s is eating..."% self.name)

	def talk(self):
		print("%s is talking..."% self.name)

class relation(object):
	def make_friend(self,obj):
		print("%s is make friend with %s"%(self.name,obj.name))

class Man(People,relation):
	def __init__(self,name,age,money):
		#People.__init__(self,name,age)
		super(Man,self).__init__(name,age)
		self.money = money
		print("%s有%s money"%(self.name,self.money))
		
	def sleep(self):
		print("%s is sleep"%self.name)

class Women(People,relation):
	def get_birth(self):
		print("%s in a born"%self.name)
	 
m1 = Man("moke",22,1200)
# m1.eat()
# m1.talk()
# m1.sleep()

w1 = Women("jes",22)
# w1.get_birth()
# w1.talk()
m1.make_friend(w1)




'''
py2 经典类》》深度优先继承，新式类》》广度优先继承
py3 经典类和新式类》》》统一广度优先继承

静态方法
	@staticmethod
	不需要self
	
	与类无关，不能访问类中的任何属性和方法
类方法
	只能访问类变量
属性@property
	把一个方法变成一个静态属性
	flight.status
	@status.setter
	flight,status=3
	@status.delter删除

反射
	getattr(obj,str)
	setattr(obj,str,val)
	hasattr(obj,str)
	delattr(obj,str)

	
特殊方法
	__doc__描述
	__module__操作的对象在那个模块
	__class__操作对象的类是什么
	
	__init__构造方法
	__del__析构方法
	
	__call__   : 对象() 类()()

	__dict__ 打印类里面的所有属性
	
	__str__默认输出该方法的返回值
	
	

	

'''