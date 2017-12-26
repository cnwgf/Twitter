#!/usr/bin/python
# -- coding: utf-8 --
'''
Created on 2017年12月11日 下午2:57:40
@author:  amir
'''
import pika
from net.httprequest import httprequest
from analyze.analyze import analyze

class twittersearch(object):

    def __init__(self,queue=''):
        self.quename = queue
        self.credentials = pika.PlainCredentials('admin','1q2w3e4r')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('47.88.60.222',credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.quename)
        pass

    def queue_sender(self,msg=''):

        self.channel.basic_publish(exchange='', routing_key = self.quename, body= msg )
        self.connection.close()
        print("[%s] Sent ok "%(self.quename))

        pass

    def twitter_user_info_(self, pasite="", pausername=""):
        scheme ="https"
        siteurl = "%s://%s/%s"%(scheme, pasite,pausername)
        http = httprequest()
        http.__setheader__(pasite, "GET", pausername, scheme)
        html = http.__send__(siteurl, http.header)

        #self.queue_sender(html)

        return html
        pass

    pass

if __name__ == '__main__':

    
    site = "www.twitter.com"
    #username = "OmgSachin"
    while True:
        username = raw_input("请输入账户：")
        if username in "exit":
            break
        else:
            twitterobj =  twittersearch('twitterque')
            html = twitterobj.twitter_user_info_(site, username)

            analy = analyze(html)
            result = analy.__GetTweeterinfo__()

            twitterobj.queue_sender(result)
        pass


