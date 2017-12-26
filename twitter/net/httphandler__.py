#!/usr/bin/python  
# -- coding: utf-8 --
'''
Created on 2017年12月14日 下午4:40:03
@author:  amir
'''
import urllib2

class httphandler__(urllib2.HTTPRedirectHandler):
    
    __cookie_flag = 'set-Cookie: '
    
    @staticmethod
    def __find_cookie(headers):

        for msg in headers:

            if msg.find(httphandler__.__cookie_flag) != -1:

                return msg.replace(httphandler__.__cookie_flag, '')
            return ''

    def http_error_301(self, req, fp, code, msg, httpmsg):

	#print  "301: ",httpmsg.headers
        cookie = httphandler__.__find_cookie(httpmsg.headers)

        if cookie != '':

            req.add_header("Cookie", cookie)

        return urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, httpmsg)

    def http_error_302(self, req, fp, code, msg, httpmsg):

	#print  "302: ",httpmsg.headers
        cookie = httphandler__.__find_cookie(httpmsg.headers)

        if cookie != '':

            req.add_header("Cookie", cookie)

        return urllib2.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, httpmsg)
    
    
