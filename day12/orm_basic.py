#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:hxmh23@127.0.0.1/testdb",encoding='utf-8',echo=False)
Base = declarative_base()   #生成orm基类

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<id:%s name:%s>" %(self.id,self.name)

Base.metadata.create_all(engine)
Session_class = sessionmaker(bind=engine)  #创建与数据库的对话session class,返回给session是个class,不是实例
Session = Session_class()  #生成session实例

# user_obj = User(name="moke",password="123456")
# user_obj2 = User(name="weat",password="123456")
# print(user_obj.name,user_obj.id)
#
# Session.add(user_obj)
# Session.add(user_obj2)
# print(user_obj.name,user_obj.id)

# data = Session.query(User).filter_by().all()		
data = Session.query(User).filter_by(id=1).first() #取第一个
print(data)
Session.commit()