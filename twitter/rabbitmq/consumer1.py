#!/usr/bin/python  
# -- coding: utf-8 --
'''
Created on 2017年12月18日 上午9:28:51
@author:  amir
    消息处理者
'''
import pika

class consumer1(object):
    def __init__(self):
        
        self.credentials = pika.PlainCredentials('admin','1q2w3e4r')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('4.88.6.22',credentials=self.credentials))
        self.channel = self.connection.channel()
        pass
    
    def callback(self,ch, method, properties, body):
        print(" [x] Received %r" % body)
        pass
    
    def basic_consumer(self,name=''):
                
        self.channel.queue_declare(queue=name)
        self.channel.basic_consume(self.callback, queue=name, no_ack=True)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        pass
    pass

if __name__ == '__main__':
    
    consumer = consumer1()
    consumer.basic_consumer('twitterque')
