#!/usr/bin/python  
# -- coding: utf-8 --
'''
Created on 2017年12月21日 下午4:05:12
@author:  amir
'''

class Timeline(object):
    
    def getimeline_(self,data=object):
        timeline = {}
        stream = data.find("div","ProfileTimeline")
        
        if stream is None: # 判断是否有时间线的推文
            timeline["None"] = "None" 
            pass
        else:
            
            #######################本个页面推文范围##############################
            if "div" in stream.decode() and "stream-container" in stream.decode():
                range = {}
                contain = stream.find("div","stream-container")

                if "data-max-position" in contain.decode() and "data-min-position" in contain.decode():
                    range["max"] = contain.attrs.get('data-max-position')
                    range["min"] = contain.attrs.get('data-min-position')
                    pass
                else:
                    range["max"] = "0"
                    range["min"] = "0"
                    pass
                pass
            
                timeline["range"] = range
            ########################提取推文范围结束##############################
            
            
            
            ########################提取推文正文部分##############################

            if "div" in stream.decode() and "stream" in stream.decode():
                contentlist = []
                streamitems = stream.find("div","stream")
                
                if streamitems is None: #判断是否有推文 
                    content = {"None"}
                    contentlist.append(content)
                    pass
                else:
                    ###########################有 OL 解析 OL 标签 开始 #############################
                    
                    if "ol" in streamitems.decode() and "stream-items js-navigable-stream" in streamitems.decode():
                        #print "ol in ... "
                        items = streamitems.find("ol",class_=["stream-items","js-navigable-stream"])
                        i = 0
                        for items_ in items.find_all("li",class_=["js-stream-item","stream-item","stream-item"] ):
                            content = {}
                            #print "len: ",i
                            if items_ is None:
                                #print " not li"
                                content = "None"
                                contentlist.append(content)
                                pass
                            else:
                                #print " in else['items_'] is li " 
                                if "js-stream-item stream-item stream-item" in items_.decode(): #普通的推文
                                    
                                    content["tweet"] = self.analyzetweet_(items_)
                                    pass
                                pass
                            pass
                            i += 1 
                            contentlist.append(content)

                        pass
                    ###########################解析 OL 标签 结束 ##################################
                    pass
                timeline["stream"] = contentlist
                pass
            ########################提取推文正文部分结束################################
            
            #print json.dumps(timeline)
            pass
        
        return timeline  # 返回时间线对象
    ########################提取推文正文部分 工作函数区域 开始###############################
    
    """
        #在LI中解析，div中包含推文头信息
    """
    def analyzetweethead_(self,data=object):
        #print "in analyzetweethead_ .... "
        head_ = {}
        if data is None:
            #print "data is none"
            head_["None"] = ""
            pass
        else:
            #print "else data-item-type: "
            if "data-item-type" in data.decode():
                head_["tweetype"] = data['data-item-type']
                pass
            
            if "div" in data.decode() and "tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet" in data.decode():
                
                headiv = data.find("div",class_=["tweet","js-stream-tweet","js-actionable-tweet","js-profile-popup-actionable","dismissible-content","original-tweet","js-original-tweet"] )
                if "data-tweet-id" in headiv.decode():
                    head_["tweetid"] = headiv['data-tweet-id']
                    pass
                
                if "data-screen-name" in headiv.decode():
                    head_["screenname"] = headiv['data-screen-name']
                    pass
                
                if "data-name" in headiv.decode():
                    head_["name"] = headiv['data-name']
                    pass
                
                if "data-user-id" in headiv.decode():
                    head_["userid"] = headiv['data-user-id']
                    pass
                
                if "data-permalink-path" in headiv.decode():
                    head_["tweeturl"] = headiv['data-permalink-path']
                    pass
                
                if "data-mentions" in headiv.decode():
                    head_["mentions"] = headiv['data-mentions']
                    pass
                pass
            
            if "div" in data.decode() and "stream-item-header" in data.decode():
                if "img" in data.decode() and "" in data.decode():
                    imgobj = data.find("img",class_=["avatar","js-action-profile-avatar"] )
                    head_["headpot"] = imgobj['src']
                    pass
                
                if "small" in data.decode() and "time" in data.decode():
                    timeobj = data.find("small",class_=["time"])
                    head_["time"] = timeobj.a['title']
                    pass
                
                pass
            
            pass
        return head_
        pass
    
    """
        #在LI中解析，div中包含推文结尾部分信息
    """
    def analyzefooter_(self,data=object):
        
        footer_ = {}
        if "div" in data.decode() and "stream-item-footer" in data.decode(): # 判断 <div class="stream-item-footer">
            
            footer = data.find("div",class_=["ProfileTweet-actionCountList","u-hiddenVisually"] ) # 获取 <div class="ProfileTweet-actionCountList u-hiddenVisually">
            
            if footer is None: # 健壮性判断
                footer_["none"] = "None"
                pass
            else:

                if "ProfileTweet-action--reply" in footer.decode():
                    reply = footer.find("span",class_=["ProfileTweet-action--reply"] )
                    #if "ProfileTweet-actionCount" in reply.decode() and "data-tweet-stat-count" in reply.decode():
                    if "span" in reply.decode() and "data-tweet-stat-count" in reply.decode():
                        #footer_["replies"] = reply.find("span",class_="ProfileTweet-actionCount")['data-tweet-stat-count']
                        footer_["replies"] = reply.span['data-tweet-stat-count']
                    
                if "ProfileTweet-action--retweet" in footer.decode():
                    retweet = footer.find("span",class_=["ProfileTweet-action--retweet"] )
                    #if "ProfileTweet-actionCount" in retweet.decode() and "data-tweet-stat-count" in retweet.decode():
                    if "span" in retweet.decode() and "data-tweet-stat-count" in retweet.decode():
                        footer_["retweets"] = retweet.span['data-tweet-stat-count']
                        
                if "ProfileTweet-action--favorite" in footer.decode():
                    favorite = footer.find("span",class_=["ProfileTweet-action--favorite"] )
                    #if "ProfileTweet-actionCount" in favorite.decode() and "data-tweet-stat-count" in favorite.decode():
                    if "span" in favorite.decode() and "data-tweet-stat-count" in favorite.decode():
                        footer_["favorite"] = favorite.span['data-tweet-stat-count']          
            pass
        
        return footer_
    
    """
    tweet js-stream-tweet js-actionable-tweet js-profile-popup-actionable dismissible-content original-tweet js-original-tweet
       只有文本信息的原文
    """
    def analyzetweet_(self,data=object):
        #print "in analyzetweet_ .... "
        tweet_ = {}
        body_ = {}
        tweetdiv = data.find("div",class_=["tweet","js-stream-tweet","js-actionable-tweet","js-profile-popup-actionable","dismissible-content","original-tweet","js-original-tweet"] )
        
        tweet_["head"] = self.analyzetweethead_(data) # 提取推文头信息
        divattrclass = tweetdiv.attrs.get('class')
        
        if "js-tweet-text-container" in tweetdiv.decode():
            body = data.find("div",class_=["js-tweet-text-container"])
            body_["txt"] = body.p.get_text()
            pass
        
        if "js-pinned" in divattrclass: # 置顶推文
            body_["top"] = "stickytweet"
            pass
        
        if "tweet-has-context" in divattrclass: # 转发别人的推文
            body_["retweet"] = self.analyzeforward_(tweetdiv)
            pass
        
        if "has-cards" in divattrclass and "has-content" in divattrclass: # 带图片、音频、视频等多媒体的推文
            body_["media"] = self.analyzehascards_(tweetdiv)
            pass
        
        if "cards-forward" in divattrclass and "has-cards" in divattrclass: # 转发推文并且是分享的其他的信息引用
            body_["quote"] = self.analyzecardsforward_(tweetdiv)
            pass

        ########################消息正文####################################
        
        
        
        ########################操作结束####################################
        
        tweet_["body"] = body_
        tweet_["footer"] = self.analyzefooter_(data) # 提取推文的关注情况
        return tweet_
        pass
    
    """
    has-cards has-content
    """
    def analyzehascards_(self, data=object):
        
        media_ = {}
        if "div" in data.decode() and "AdaptiveMediaOuterContainer" in data.decode():
            media = data.find("div",class_=["AdaptiveMediaOuterContainer"] )
            
            if "img" in media.decode() and "data-aria-label-part" in media.decode():
                imgobj_ = []
                
                for img in media.find_all("div",class_=["AdaptiveMedia-photoContainer","js-adaptive-photo"]):
                    
                    if img is None:
                        imgobj_["None"] = ""
                        pass
                    else:
                        imgobj_.append(img['data-image-url'])
                        pass
                    
                    pass
                media_["image"] = imgobj_
            
            if "img" in media.decode() and "data-aria-label-part" in media.decode(): 
                pass
            
            pass
        
        return media_
        
        pass

    """
    has-cards cards-forward
    """
    def analyzecardsforward_(self, data=object):
        
        quote_ = {}
        
        if "data-card2-type" in data.decode():
            
            card2 = data.attrs.get('data-card2-type')
            
            carddiv = data.find("div",attrs={"data-card2-name":card2} )
            
            if carddiv is None:
                quote_["None"] = ""
                pass
            else:
                quote_["url"] = carddiv.div.attrs.get('data-card-url')# 
                quote_["pubid"] = carddiv.div.attrs.get('data-publisher-id')#data-publisher-id
                quote_["cardname"] = carddiv.div.attrs.get('data-card-name')#data-card-name="player"
                pass
            pass
        return quote_
        pass
    
    """
     tweet-has-context 转发的推文消息
    """
    def analyzeforward_(self, data=object):
        
        retweet = {}
        if "QuoteTweet" in data.decode() and "js-tweet-details-fixer" in data.decode():
            
            retwe = data.find("div",class_=["QuoteTweet-container"])
            
            if retwe is None:
                retweet["None"] = "None"
                pass
            else:
                
                if "div" in retwe.decode() and "QuoteTweet-innerContainer u-cf js-permalink js-media-container" in retwe.decode(): 
                    retmp = retwe.find("div",class_=["QuoteTweet-innerContainer","u-cf","js-permalink","js-media-container"] )
                    
                    if retmp is None:
                        retweet["None"] = "None"
                        pass
                    else:
                        if "data-item-id" in retmp.decode():
                            retweet["retweetid"] = retmp.attrs.get('data-item-id')
                            pass
                        
                        if "data-item-type" in retmp.decode():
                            retweet["retweetype"] = retmp.attrs.get('data-item-type')
                            pass
                        
                        if "data-screen-name" in retmp.decode():
                            retweet["rescreenname"] = retmp.attrs.get('data-screen-name')
                            pass
                        
                        if "data-user-id" in retmp.decode():
                            retweet["reuserid"] = retmp.attrs.get('data-user-id')
                            pass
                        
                        if "href" in retmp.decode():
                            retweet["retweeturl"] = retmp.attrs.get('href')
                            pass
                        
                        pass
                    
                    if "div" in retmp.decode() and "tweet-content" in retmp.decode():
                        if "div" in retmp.decode() and "QuoteTweet-text tweet-text u-dir js-ellipsis" in retmp.decode(): 
                            ltrobj = retmp.find("div",class_=["QuoteTweet-text","tweet-text","u-dir","js-ellipsis"] )
                            retweet["retweetxt"] = ltrobj.get_text()
                            pass
                        pass
                    
                    pass
            return retweet
            pass
        
        pass
    
    
    ########################提取推文正文部分 工作函数区域 结束###############################

    pass

#if __name__ == '__main__': # 测试代码块程序
#    #   
#    soup = BeautifulSoup(Htmlsrc.html,'html5lib')
#    timeline = Timeline()
#    
#    htmldata = timeline.getimeline_(soup)
#    print json.dumps(htmldata)
#    
#    pass
#
