#!/usr/bin/python
# -- coding: utf-8 --
'''
Created on 2017年12月11日 下午2:49:17
@author:  amir
'''
import json
import utiler
import ProfileHeader
import ProfileTimeline

from bs4 import BeautifulSoup

class analyze(object):

    def __init__(self,data):
        self.data = data
        self.utilobj = utiler.utiler(data)
        self.tweinfo = {}
        pass

    def Baseheaderinfo(self):
        
        baseinfo = {}
        htmlobj = BeautifulSoup(self.data,'html5lib')
        
        soup = htmlobj.find("div",class_=["ProfileHeaderCard"] )
        
        if soup is None:
            baseinfo["Unknown"] = ""
            pass
        else:
            headutil = ProfileHeader.ProfileHeader()
            baseinfo["HomeUrl"] = headutil.gethomeurl_(soup)
            baseinfo["JoinDate"] = headutil.getjoinDate_(soup)
            baseinfo["BirthDate"] = headutil.getbirthdate_(soup)
            baseinfo["Location"] = headutil.getlocation_(soup)
            baseinfo["Describe"] = headutil.getdescribe_(soup)
            baseinfo["ScreenName"] = headutil.getscreenname_(soup)
            baseinfo["Name"] = headutil.getname_(soup)
            baseinfo["Periscope"] = headutil.getperiscope_(soup)
            baseinfo["followinfo"] = headutil.getuserpopularity_(soup)
            pass
       
        return baseinfo
        
        pass
    
    def __GetProfile__(self):
        self.tweinfo["baseinfo"] = self.Baseheaderinfo()
        pass

    def __GetTweetContent__(self):

        htmlobj = BeautifulSoup(self.data,'html5lib')
        
        self.tweinfo["top20"] = ProfileTimeline.Timeline().getimeline_(htmlobj)
        pass

    def __GetTweeterinfo__(self):
        self.__GetProfile__()
        self.__GetTweetContent__()

        return json.dumps(self.tweinfo)
        pass


