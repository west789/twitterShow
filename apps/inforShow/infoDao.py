from .models import *
import re
pattern = re.compile("https?://.*?[\s]|https?://.*?$")
#获取main模板里面数据信息
def get_specifyInfo(accountId):
    if accountId != 0:
        accountInfo = account.objects.filter(accountId=accountId)
        accountDict = {}
        accountDict["accountId"] = accountInfo[0].accountId
        accountDict["accountName"] = accountInfo[0].accountName
        accountDict["screenName"] = accountInfo[0].screenName
        accountDict["location"] = accountInfo[0].location if accountInfo[0].location else ""
        accountDict["statusesCount"] = accountInfo[0].statusesCount
        accountDict["friendsCount"] = accountInfo[0].friendsCount
        accountDict["favoritesCount"] = accountInfo[0].favoritesCount
        accountDict["followersCount"] = accountInfo[0].followersCount
        accountDict["profileImage"] = accountInfo[0].profileImage
        accountDict["description"] = accountInfo[0].description
        accountDict["bannerUrl"] = accountInfo[0].bannerUrl if accountInfo[0].bannerUrl else "homeback.jpg"
        accountDict["url"] = accountInfo[0].url if accountInfo[0].url else ""
        accountDict["accountTime"] = accountInfo[0].accountTime.strftime("%Y-%m-%d")
        return accountDict
    else:
        return getFixInfo()

#获取content模板里面的数据信息
def getTweetsList(tweetsInfo):
    tweetsList = []
    for item in tweetsInfo:
        itemDict = {}
        itemTweetsText = getTextUrl(item.tweetsText)
        itemDict["tweetsText"] = itemTweetsText[0]
        itemDict["txtUrl"] = itemTweetsText[1]
        itemDict["tweetsUrl"] = item.tweetsUrl
        itemDict["imageUrl"] = item.imageUrl if item.imageUrl is not None else ""
        itemDict["videoUrl"] = item.videoUrl if item.videoUrl is not None else ""
        itemDict["retweetCount"] = item.retweetCount
        itemDict["tweetFavCount"] = item.tweetFavCount
        itemDict["tweetTime"] = item.tweetTime.strftime("%Y-%m-%d %H:%M")
        itemDict["accountName"] = item.accountId.accountName
        itemDict["screenName"] = item.accountId.screenName
        itemDict["profileImage"] = item.accountId.profileImage
        tweetsList.append(itemDict)
    return tweetsList


#添加静态文件信息
def getFixInfo():
    accountDict = {}
    accountDict["accountId"] = 0
    accountDict["accountName"] = "Availink"
    accountDict["screenName"] = "Availink"
    accountDict["location"] = "Beijing"
    accountDict["statusesCount"] = ""
    accountDict["friendsCount"] = ""
    accountDict["favoritesCount"] = ""
    accountDict["followersCount"] = ""
    accountDict["profileImage"] = "fixhead.jpg"
    accountDict["description"] = '''Lead by internationally renowned IC technologists, Availink has been widely acknowledged by its customers as a 
                                    “demodulator expert” since its inception. In 2008, the company’s first demodulator chip contributed tremendously 
                                    to the success of early-stage direct-to-home satellite TV broadcasting, enabling dozens of home entertainment 
                                    programs to reach millions of households in remote and mountainous countryside in China.'''
    accountDict["bannerUrl"] = "homeback.jpg"
    accountDict["url"] = ""
    accountDict["accountTime"] = "2010-01-01"
    return accountDict

#分割tweetsText中的链接
def getTextUrl(handle_text):
    try:
        express = "https?://.*?[\s]|https?://.*?$"
        pattern = re.compile(express)
        txtUrl = pattern.findall(handle_text)[0].strip()
        tweetsText = pattern.sub('', handle_text).strip()
    except Exception as e:
        tweetsText = handle_text
        txtUrl = ""
    finally:
        return (tweetsText, txtUrl)