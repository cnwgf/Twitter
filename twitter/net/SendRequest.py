#!/usr/bin/python
# -- coding: utf-8 --
'''
Created on 2017年12月11日 下午2:47:16
@author:  amir
'''

#import base64
#import urllib
import urllib2
import zlib
from httphandler__ import httphandler__

from abc import ABCMeta,abstractmethod

class SendRequest(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __setheader__(self):
        pass

    def __send__(self, url='', header=object):
        request = urllib2.Request(url,headers=header)

        opener = urllib2.build_opener(httphandler__())
        response = opener.open(request, timeout=6)
        gzip = response.headers.get("content-encoding")

        if gzip:
            htmlobj = response.read()
            htmlobj = zlib.decompress(htmlobj, 16+zlib.MAX_WBITS)
            
        else:
            htmlobj = response.read()
            pass

        return htmlobj

