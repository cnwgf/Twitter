#!/usr/bin/python  
# -- coding: utf-8 --
'''
Created on 2017年12月20日 下午3:03:19
@author:  amir
'''

html ="""

"""

class ProfileHeader(object):
    
    """
    <h1 class="ProfileHeaderCard-name"></h1>
    """
    def getname_(self, data=object):
        result  = {}
        name = data.find("h1",class_=["ProfileHeaderCard-name"])
        
        if name is None:
            result = "Unknown"
            pass
        else:
            if "a" in name.decode() and "ProfileHeaderCard-nameLink u-textInheritColor js-nav" in name.decode():
                result["name"] = name.find("a",class_=["ProfileHeaderCard-nameLink","u-textInheritColor","js-nav"]).get_text().encode("utf-8")
                typename = name.find("a", class_=["js-tooltip"])
                
                if typename is None:
                    result["type"] = "Unverified"
                    pass
                else:
                    result["type"] = typename.get_text().encode("utf-8")
                    pass
                pass
            else:
                result = "Unknown"
                pass
            pass
        
        return result
        
        pass
    
    """
    <h2 class="ProfileHeaderCard-screenname u-inlineBlock u-dir" dir="ltr">
    """
    def getscreenname_(self,data=object):
        screenname_ = ""
        screenname = data.find("h2",class_=["ProfileHeaderCard-screenname","u-inlineBlock","u-dir"])
        
        if screenname is None:
            screenname_ = "Unknown"
            pass
        else:
            if "span" in screenname.decode() and "username u-dir" in screenname.decode():
                screenname_ = screenname.span.get_text().encode("utf-8")
                pass
            else:
                screenname_ = "Unknown"
                pass
            pass
        
        return screenname_
        
        pass
    
    """
    <p class="ProfileHeaderCard-bio u-dir" dir="ltr">
    """
    def getdescribe_(self,data=object):
        describe_ = ""
        describe = data.find("p",class_=["ProfileHeaderCard-bio","u-dir"])
        
        if describe is None:
            describe_ = "Unknown"
            pass
        else:
            describe_ = describe.get_text().encode("utf-8")
            pass
        
        return describe_
        
        pass
    
    """
    <div class="ProfileHeaderCard-location ">
    """
    def getlocation_(self,data=object):
        
        location_ = ""
        location = data.find("div",class_=["ProfileHeaderCard-location"])
        
        if location is None:
            location_ = "Unknown"
            pass
        else:
            if "span" in location.decode() and "ProfileHeaderCard-locationText" in location.decode():
                spantxt = location.find("span",class_=["ProfileHeaderCard-locationText","u-dir"])
                location_ = spantxt.get_text().encode("utf-8")
                pass
            else:
                location_ = "Unknown"
                pass

            pass
        
        return location_
        
        pass
    
    """
    div class="ProfileHeaderCard-url  u-hidden">
    """
    def gethomeurl_(self,data=object):
        url_ = ""
        homeurl = data.find("div",class_=["ProfileHeaderCard-url","u-hidden"])
        
        if homeurl is None:
            url_ = "Unknown"
            pass
        else:
            spantxt = homeurl.find("span",class_=["ProfileHeaderCard-urlText","u-dir"])

            if "a" in spantxt.decode() and "title" in spantxt.decode():
                url_ = spantxt.a['title'].encode("utf-8")
                pass
            else:
                url_ = spantxt.get_text().encode("utf-8")
                pass
            pass
        
        return url_;
        pass
    
    """
    <div class="ProfileHeaderCard-joinDate">
    """
    def getjoinDate_(self, data=object):
        date_ = ""
        joindate = data.find("div",class_=["ProfileHeaderCard-joinDate"] )
        
        if joindate is None:
            date_ = ("Unknown")
            pass
        else:
            if "ProfileHeaderCard-joinDateText" in joindate.decode() and "title" in joindate.decode():
                spantxt = joindate.find("span",class_=["ProfileHeaderCard-joinDateText","js-tooltip","u-dir"])
                date_ = (spantxt['title'].encode("utf-8"))
                pass
            else:
                date_ = ("Unknown")
                pass
            pass
        return date_
        pass
    
    """
    <div class="ProfileHeaderCard-birthdate u-hidden">
    """
    def getbirthdate_(self, data=object):
        
        birthdate_ = ""
        birthdate = data.find("div",class_=["ProfileHeaderCard-birthdate","u-hidden"])
        
        if birthdate is None:
            birthdate_ = "Unknown"
            pass
        else:
            
            if "span" in birthdate.decode() and "ProfileHeaderCard-birthdateText" in birthdate.decode():
                
                spantxt = birthdate.find("span",class_=["ProfileHeaderCard-birthdateText","u-dir"])
                birthdate_ = spantxt.get_text().encode("utf-8")
                pass
            else:
                pass
            
            pass
        
        return birthdate_
        pass
    
    """
    <div class="ProfileHeaderCard-periscopeProfile ">
    """
    def getperiscope_(self, data=object):
        
        periscope_ = ""
        periscope = data.find("div","ProfileHeaderCard-periscopeProfile")
        
        if periscope is None:
            periscope_ = "Unknown"
            pass
        else:
            if "a" in periscope.decode() and "ProfileHeaderCard-periscopeProfileTextLive u-textUserColor" in periscope.decode():
                
                aobj = periscope.find("a",class_=["ProfileHeaderCard-periscopeProfileTextLive","u-textUserColor"] )
                periscope_ = aobj['href'].encode("utf-8")
                pass
            pass
        
        pass
        
        return periscope_
    
    def getuserpopularity_(self, data=object):

        followinfo = {}
        
        for followobj in data.find_all("div", class_=["ProfileNav"] ):
            if followobj is None:
                followinfo["None"] = "None"
                pass
            else:
                if "data-user-id" in followobj.decode():
                    followinfo["userid"] = followobj['data-user-id']
                    pass
                    
                followinfo["tweets"] = followobj.find("li","ProfileNav-item--tweets").a.find("span","ProfileNav-value")['data-count']
                followinfo["following"] = followobj.find("li","ProfileNav-item--following").a.find("span","ProfileNav-value")['data-count']
                followinfo["followingurl"] = followobj.find("li","ProfileNav-item--following").a['href']
                followinfo["followers"] = followobj.find("li","ProfileNav-item--followers").a.find("span","ProfileNav-value")['data-count']
                followinfo["followersurl"] = followobj.find("li","ProfileNav-item--followers").a['href']
                followinfo["favorites"] = followobj.find("li","ProfileNav-item--favorites").a.find("span","ProfileNav-value")['data-count']
                followinfo["favoritesurl"] = followobj.find("li","ProfileNav-item--favorites").a['href']
                pass
            pass

        return (followinfo) 
    
    pass

#if __name__ == '__main__':
#    #   
#    soup = BeautifulSoup(html,'html5lib')
#    headutil = ProfileHeader()
#    
#    print "HomeUrl: ",headutil.gethomeurl_(soup)
#    print "JoinDate: ",headutil.getjoinDate_(soup)
#    print "BirthDate: ",headutil.getbirthdate_(soup)
#    print "Location: ",headutil.getlocation_(soup)
#    print "Describe: ",headutil.getdescribe_(soup)
#    print "ScreenName: ",headutil.getscreenname_(soup)
#    print "Name: ",headutil.getname_(soup)
#    
#    print "Popularity: ",headutil.getuserpopularity_(soup)
    
    
#    pass


