#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters('localhost'))

channel = connection.channel()
channel.exchange_declare(exchange='logs',
                      exchange_type='fanout')

result = channel.queue_declare(exclusive=True)          #唯一的
queue_name = result.method.queue
print("queue_name:",queue_name)

channel.queue_bind(exchange='logs',
                   queue=queue_name)
print("waiting for logs, to exit press CTRL + C")

def callback(ch,method,properties,body):
    print("-->",ch,method,properties)
    # time.sleep(10)
    print("Received %r"% body)

channel.basic_consume(callback,
                    queue=queue_name,
                    no_ack=True)

channel.start_consuming()