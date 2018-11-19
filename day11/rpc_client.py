#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import pika
import uuid

class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            host='localhost'))
        self.channel = self.connection.channel()                    #声明一个管道
        result = self.channel.queue_declare(exclusive=True)        #声明queue
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True,   #s收到消息就调用on_response
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                                                    reply_to=self.callback_queue,
                                                                    correlation_id=self.corr_id,),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()           #非阻塞版的start_consume
            # print("no msg...")
        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()

print(" [x] Requesting fib(20)")
response = fibonacci_rpc.call(20)
print(" [.] Got %r" % response)