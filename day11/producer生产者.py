#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(
	pika.ConnectionParameters('localhost')
	)
channel = connection.channel() 		   #声明一个管道
channel.queue_declare(queue='hello',durable=True)   #声明queue   队列持久化

channel.basic_publish(exchange='',     #
					routing_key='hello',            #queue名字
					body='hello world!',			#消息内容
					properties=pika.BasicProperties(
					delivery_mode=2,))				#消息持久化 make message persistent
					
print("send hello world")

connection.close()