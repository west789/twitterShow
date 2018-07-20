from django.db import models

# Create your models here.
#Talbe account

class account(models.Model):
    accountId = models.AutoField(primary_key=True)
    accountName = models.CharField(max_length=200, )
    twitterId = models.CharField(max_length=200, )
    screenName = models.CharField(max_length=200, )
    location = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    profileImage = models.CharField(max_length=200, null=True, blank=True)
    bannerUrl = models.CharField(max_length=200, null=True, blank=True)
    statusesCount = models.IntegerField(null=True, blank=True)
    friendsCount = models.IntegerField(null=True, blank=True)
    followersCount = models.IntegerField(null=True, blank=True)
    favoritesCount = models.IntegerField(null=True, blank=True)
    accountTime = models.DateTimeField(null=True, blank=True)
    class Meta():
        db_table = 'account'

#Table tweets

class tweets(models.Model):
    tweetsId = models.AutoField(primary_key=True)
    accountId = models.ForeignKey("account", on_delete=models.CASCADE, db_column="accountId")
    tweetsText = models.TextField()
    tweetsUrl = models.CharField(max_length=200, null=True, blank=True)
    twitterId = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=200, null=True, blank=True)
    videoUrl = models.CharField(max_length=200, null=True, blank=True)
    retweetCount = models.IntegerField(null=True, blank=True)
    tweetFavCount = models.IntegerField(null=True, blank=True)
    tweetTime = models.DateTimeField(null=True, blank=True)
    class Meta():
        db_table = 'tweets'