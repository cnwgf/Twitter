#!/usr/bin/python  
# -- coding: utf-8 --
'''
Created on 2017年12月11日 下午2:47:16
@author:  amir
'''
from bs4 import BeautifulSoup
import twebconst
import json

class utiler(object):
    
    def __init__(self,data=""):
        self.soup = BeautifulSoup(data,'html5lib')
        self.probj = twebconst.web_profile()
        pass
    
    def intercept(self,data=object,key='',value=''):
        pass
    
    """
        ProfileHeaderCard = "ProfileHeaderCard"
        wall = '-'
        url ="url"
        name = "name"
        biostate = "biostate"
        location = "location"
        joinDate = "joinDate"
        birthdate = "birthdate"
        screenname = "screenname"
    """
    def GetProfileHeaderCard(self):
        i = 0
        baseinfo = [{}] 

        for headitem in self.soup.find_all("div", class_=self.probj.ProfileHeaderCard):
            
            baseinfo[i][self.probj.name] = headitem.h1.a.get_text()
            baseinfo[i][self.probj.screenname] = headitem.h2.a.span.b.string
            baseinfo[i][self.probj.biostate] = headitem.p.get_text()
            baseinfo[i][self.probj.location] = headitem.find("div",self.location()).find("span",class_=self.locationText()).string
            baseinfo[i][self.probj.url] = headitem.find("div",self.url()).find("span",class_=self.urlText()).a['href']
            baseinfo[i][self.probj.joinDate] = headitem.find("div",self.joinDate()).find("span",class_=self.joinDateText())['title']
            baseinfo[i][self.probj.birthdate] = headitem.find("div",self.birthdate()).find("span",class_=self.birthdateText()).string
            i += 1
            pass
        
        i = 0    
	print json.dumps(baseinfo)
        return baseinfo
        
    """
        ProfileNav = 'ProfileNav'
        tweets = 'tweets'
        following = 'following'
        followingurl = 'followingurl'
        followers = 'followers'
        followersurl = 'followersurl'
        favorites = 'favorites'
        favoritesurl = 'favoritesurl' 
        navwall = '-item--'
    """
    def GetProfileNav(self):
        i = 0
        followinfo = [{}]
        
        for followobj in self.soup.find_all("div", class_=self.probj.ProfileNav):
            
            followinfo[i][self.probj.tweets] = followobj.find("li","ProfileNav-item--tweets").a.find("span","ProfileNav-value")['data-count']
            followinfo[i][self.probj.following] = followobj.find("li","ProfileNav-item--following").a.find("span","ProfileNav-value")['data-count']
            followinfo[i][self.probj.followingurl] = followobj.find("li","ProfileNav-item--following").a['href']
            followinfo[i][self.probj.followers] = followobj.find("li","ProfileNav-item--followers").a.find("span","ProfileNav-value")['data-count']
            followinfo[i][self.probj.followersurl] = followobj.find("li","ProfileNav-item--followers").a['href']
            followinfo[i][self.probj.favorites] = followobj.find("li","ProfileNav-item--favorites").a.find("span","ProfileNav-value")['data-count']
            followinfo[i][self.probj.favoritesurl] = followobj.find("li","ProfileNav-item--favorites").a['href']
            i += 1
            pass
        
        i = 0
	print json.dumps(followinfo)
        return (followinfo) 
    
    def GetContentList(self):

        """
                                    获取当前页面推文ID范围                        
        """
        range = {}
        range["max"]=self.soup.find("div", "stream-container")['data-max-position']
        range["min"]=self.soup.find("div", "stream-container")['data-min-position']
              
        container = self.soup.find("div", class_="stream-container") 
           
        contentlist = []
        for containli in container.find_all("li",class_=["js-stream-item","stream-item","stream-item"] ):
            
            content = {}
            content["tweet"] =self._explaincontent(containli)#<div class="stream-item-header">
            contentlist.append(content)
            pass
	
        return (contentlist) 

    
    ##############################################################################################
    """
                    tweet内容解析器：
                                                                            分为 内容头，
                                                                            内容正文， 
                                                                            推文的关注情况
    """
    def _explaincontent(self, data=object):
        content ={}
        content["tweet_id"] = data["data-item-id"].encode("utf-8")
        content["tweet_type"] = data['data-item-type'].encode("utf-8")
            
        infomp = data.find("div",class_=["tweet","js-stream-tweet","js-actionable-tweet","js-profile-popup-actionable"] )
        content["user_name"] = infomp['data-name'].encode("utf-8")
        content["user_id"] = infomp['data-user-id'].encode("utf-8")
        content["screen-name"] = infomp["data-screen-name"].encode("utf-8")
        
        bodyhead = data.find("div",class_=["stream-item-header"])
        content["portrait"] = bodyhead.find("img",class_=["avatar","js-action-profile-avatar"] )['src'].encode("utf-8")
        
	usertype = bodyhead.find("span",class_=["u-hiddenVisually"] )
        
        if usertype is None:
            content["usertype"] = 'Not verified'
        else:
            content["usertype"] = usertype.string.encode("utf-8")
        
        bodyhamp = bodyhead.find("small",class_=["time"] )

	if bodyhamp is None:
		content["time"] =  ""
                content["tweet_url"] =  ""
	else:
        	content["time"] =  bodyhamp.a['title']
        	content["tweet_url"] =  bodyhamp.a['href']
        
        body = data.find("div",class_=["js-tweet-text-container"])
	if body is None:
		pass
	else:
        	content["tweet_txt"] = body.find("p",class_=["TweetTextSize","TweetTextSize--normal","js-tweet-text","tweet-text"]).get_text().encode("utf-8")

        	for footer in data.find_all("div",class_=["ProfileTweet-actionCountList","u-hiddenVisually"]):
            
            		reply = footer.find("span",class_=["ProfileTweet-action--reply"] )
            		content["replies"] = reply.find("span",class_="ProfileTweet-actionCount")['data-tweet-stat-count'].encode("utf-8")
        
            		retweet = footer.find("span",class_=["ProfileTweet-action--retweet"] )
            		content["retweets"] = retweet.find("span",class_="ProfileTweet-actionCount")['data-tweet-stat-count'].encode("utf-8")
        
            		favorite = footer.find("span",class_=["ProfileTweet-action--favorite"] )
            		content["favorite"] = favorite.find("span",class_="ProfileTweet-actionCount")['data-tweet-stat-count'].encode("utf-8")
            
            	pass
	pass
        
        return content
    
    def _explainhead(self,data=''):
        # div class="stream-item-header"
        
        
        
        pass
    
    
    ##############################################################################################
    
    ##############################################################################################
    '''
                  账户配置信息名称
    '''        
    def location(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.location)
        pass
    
    def url(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.url)
        pass
    
    def joinDate(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.joinDate)
        pass
    
    def birthdate(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.birthdate)
        pass
    
    ##############################################################################################
    '''
                  账户配置信息class样式名称
    ''' 
    def locationText(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.location,"Text")
        pass
    
    def urlText(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.url,"Text")
        pass
    
    def joinDateText(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.joinDate,"Text")
        pass
    
    def birthdateText(self):
        return self.webkey(self.probj.ProfileHeaderCard,'-',self.probj.birthdate,"Text")
        pass
    
    def webkey(self, befor="", wall="", key="", after =""):
        return "%s%s%s%s"%(befor,wall,key,after)
        pass
    
    ##############################################################################################
    
