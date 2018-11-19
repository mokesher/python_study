import os

goods = [["iphone",5999],["apple",25],["pear",15],["beach",90]]

def show():
	count = 1
	for shop,price in goods:
		print("%s 商品：%s  价格：%s"%(count,shop,price))
		count += 1
	
def run(money):
	flag = True
	show()	
	while flag:
		choice = input("选择你要买的商品编号(如果推出，按q)：")
		if choice == "q":
			break
		elif choice.isdigit():
			choice = int(choice)
			if choice <= len(goods):
				money = int(money) - goods[choice-1][1]
				if money < 0 :
					print("余额不够，重新选择")
					money += goods[choice-1][1]
					continue
				if money > 0:
					print("成功购买，您的余额为%s"%money)
			else:
				continue
		else:
			print("输入错误，重新输入")
			




if __name__ == "__main__":
	while 1:
		money = input("请输入您的余额：")
		if money.isdigit():
			break
		else:
			print("输入错误，重新输入")
			continue
	run(money)
	
	
	
	