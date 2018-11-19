#author：moke
from getpass import getpass
import os

def user_dict():
	with open("user_info.txt","r") as f:
			for i in f:
				i.strip()
				print(i)	
def login():
	count = 0
	while count<3:
		_user = input("请输入用户名:")
		_password = getpass("请输入密码:")	 
		with open("login.txt",'r') as f:
			for line in f:
				if _user in line:
					print("您已被锁定登录")
					return 
		if _user == user and _password == pwd:
			print("登录成功！")
			break
		else:
			with open("login.txt",'a+') as f:
				f.write(_user)
				f.close()
			count += 1
			print("输入错误！请重新输入")
			continue
	else:
		print("输入次数过多，您已被锁定登录")

	
if __name__ == "__main__":
	# login()
	user_dict()