class School(object):
	def __init__(self,name,addr):
		self.name = name
		self.addr = addr
		self.student = []
		self.teacher = []

	def enroll(self,stu_obj):
		print("为学员%s注册"%stu_obj)

class SchoolMember(object):
	"""docstring for SchoolMember"""
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def tell(self):
		pass	

class Teacher(SchoolMember):
	"""docstring for Teacher"""
	def __init__(self, name,age,sex,salary,course):
		super(Teacher, self).__init__(name,age,sex)
		self.salary = salary
		self.course = course

	def tell(self):
		print('''
		---info of Teacher---
		Name:%s
		Age:%s
		Sex:%s
		Salary:%s
		Course:%s	
			'''%(self.name,self.age,self.sex,self.salary,self.course))

class Student(SchoolMember):
	"""docstring for Student"""
	def __init__(self, name,age,sex,):
		super(Student, self).__init__(name,age,sex)
	
	def tell(self):
		print('''
		---info of Student---
		Name:%s
		Age:%s
		Sex:%s
			'''%(self.name,self.age,self.sex))
		
school = School("oldboy","da")

T1 = Teacher("alex",18,"M",111,"linux")

S1 = Student("a1",19,"M")

T1.tell()
S1.tell()