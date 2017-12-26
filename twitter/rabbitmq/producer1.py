#!/usr/bin/python
# -- coding: utf-8 --
'''
Created on 2017年12月18日 上午9:27:50
@author:  amir
    消息创建者
'''
import pika

class producer1(object):

    def __init__(self):

        self.credentials = pika.PlainCredentials('admin','1q2w3e4r')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('4.88.6.22',credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='basequeue')
        self.channel.basic_publish(exchange='', routing_key='basequeue', body='Hello World!')

        print("[x] Sent 'Hello World! ' ")

        self.connection.close()

        pass

    pass

if __name__ == '__main__':

    producer1()
