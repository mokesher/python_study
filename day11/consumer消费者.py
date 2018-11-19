#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pika,time

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.queue_declare(queue='hello',durable=True)

def callback(ch,method,properties,body):
    print("-->",ch,method,properties)  #内存对象地址 、发给某个queue的信息、
    #time.sleep(10)
    print("Received %r"% body)
    ch.basic_ack(delivery_tag=method.delivery_tag)     #确认收到消息，queue中删除消息

channel.basic_qos(prefetch_count=1)      #处理这条，继续下一条---公平分发
channel.basic_consume(callback,         #如果收到消费消息，调用callback函数处理消息
                    queue='hello',
                    #no_ack=True        #True服务器不关心收没收到消息
                      )
print("waiting for messages")
channel.start_consuming()