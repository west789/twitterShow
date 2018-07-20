from django.shortcuts import render, render_to_response, redirect
from django.urls import reverse
from django.core import serializers
from .models import *
from django.http import HttpResponse, JsonResponse
from .infoDao import *


# Create your views here.
def index(request):
    # return render(request, "content.html", )
    return redirect(reverse("show:detailaccount", args=[0]))
#错误页面
def page_not_found(request):
    return render_to_response('404.html')
# 展示用户列表
def userList(request):
    return render(request, "userList.html")


# 获取用户列表数据
def get_userlist(request):
    # userlistInfo = serializers.serialize("json", account.objects.all())
    limit = int(request.GET.get("limit"))
    page = int(request.GET.get("page"))
    startRecord = (page - 1) * limit
    endRecord = limit * page
    userlistInfo = account.objects.all()
    userlistInfoSplit = userlistInfo[startRecord:endRecord]
    userList = []
    for item in userlistInfoSplit:
        itemDict = {}
        itemDict["accountId"] = item.accountId
        itemDict["accountName"] = item.accountName
        itemDict["screenName"] = item.screenName
        itemDict["statusesCount"] = item.statusesCount
        itemDict["friendsCount"] = item.friendsCount
        itemDict["favoritesCount"] = item.favoritesCount
        itemDict["followersCount"] = item.followersCount
        itemDict["accountTime"] = item.accountTime.strftime("%Y-%m-%d %H:%M")
        userList.append(itemDict)
    context = {"code": 0, "msg": "", "count": userlistInfo.count(), "data": userList}
    return JsonResponse(context)


# 获取指定用户的信息
def specifyaccount(request):
    accountId = request.session.get("accountId", default=0)
    if accountId != 0:
        accountDict = get_specifyInfo(accountId)
        return JsonResponse(accountDict)
    else:
        return ""


# 获取指定用户的twitter信息
def detailaccount(request, accountId):
    request.session["accountId"] = accountId
    # tweetsInfo = tweets.objects.filter(accountId=accountId).order_by("-tweetsId")
    accountDict = get_specifyInfo(accountId)
    # tweetsList = getTweetsList(tweetsInfo) "tweetsList": tweetsList,
    context = {"code": 200, "msg": "", "accountInfo": accountDict}
    return render(request, "content.html", context)
    # return JsonResponse(context)


# 获取所有twitter信息
def getAllTweets(request, pageNumber):
    # request.session.flush() , "accountInfo":accountDict
    accountId = request.session.get("accountId")
    if accountId == 0:
    # accountDict = get_specifyInfo(accountId)
        tweetsCount = tweets.objects.all().count()
        remainCount = tweetsCount - pageNumber * 10
        tweetsInfo = tweets.objects.all().order_by("-tweetTime")[(pageNumber - 1) * 10:pageNumber * 10]
    else:
        tweetsCount = tweets.objects.filter(accountId=accountId).count()
        remainCount = tweetsCount - pageNumber * 10
        tweetsInfo = tweets.objects.filter(accountId=accountId).order_by("-tweetsId")[
                     (pageNumber - 1) * 10:pageNumber * 10]
    tweetsList = getTweetsList(tweetsInfo)
    context = {"code": 200, "msg": "", "tweetsList": tweetsList, "remainCount": remainCount}
    # return render(request, "content.html", context)
    return JsonResponse(context)
