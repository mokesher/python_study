user_status = False
def login(func): #把要执行的模块从这里传进来
 
    def inner(*args,**kwargs):#再定义一层函数
        _username = "alex" #假装这是DB里存的用户信息
        _password = "1" #假装这是DB里存的用户信息
        global user_status
 
        if user_status == False:
            username = input("user:")
            password = input("pasword:")
 
            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")
 
        if user_status == True:
            func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
 
    return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

def home():
    print("---首页----")
@login
def japan(people):
    print("----日韩专区----")
    print("%s和你一起p"%(people))
 
def henan():
    #login() #执行前加上验证
    print("----河南专区----")

home()
# japan = login(japan) 
japan("天海")