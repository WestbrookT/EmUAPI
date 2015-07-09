import json
import requests

#
# This api uses base urls that grab data in a json format here they are:
# http://empeopled.com/topics-all
# http://empeopled.com/topic/feed?sid=A_NUMBER
# sid corresponds to a specific topic, this can be found with getTopicSID()
#


req = requests.get("http://empeopled.com/topics-all", headers={'User-Agent': 'Chrome/18.0.1025.133'})
topics = req.json()

def getAllTopics():
    #
    # This returns a list of all topic objects
    #
    return topics['data']['topics']


def getAllTopicKeys():
    #
    # This returns a dictionary of all keys that are used per topic.
    #
    return topics['data']['topics'][0].keys()

def getTopicSID(topic):
    #
    # This returns the SID of the topic name passed in
    # if its not found it returns -1
    #
    # SID is part of the url of the topic e.g.: http://empeopled.com/topic/feed?sid=368
    # Each SID corresponds to a single topic
    #
    for i in topics['data']['topics']:
        if i['name'] == topic:
            return i['sid']
    return -1

def getAllTopicNames():
    #
    # Returns a list of all topic names
    #
    names = []
    for topic in topics['data']['topics']:
        names.append(topic['name'])
    return names

def getTopicFeed(topic, pageNumber):
    #
    # Returns list of all posts on a topics feed for that page
    #
    sid = getTopicSID(topic)
    feed = requests.get("http://empeopled.com/topic/feed?page={0}&sortby=2&sid={1}".format(pageNumber, sid), headers={'User-Agent': 'Chrome/18.0.1025.133'})
    feedPage = feed.json()
    return feedPage['data']['posts']

def getFeedKeys():
    #
    # Returns a list of all key usable with getTopicFeed()
    #
    return getTopicFeed('Welcome To Empeopled', 1)[0].keys()

def getNotifications(pageNumber):
    #
    # Returns a list of all replys on that page
    #
    # https://empeopled.com/notifications/feed?page=1
    #
    # Not fully implemented yet, requires Authentification
    request = requests.get("http://empeopled.com/notifications/feed?page={}".format(pageNumber), headers={'User-Agent': 'Chrome/18.0.1025.133'})
    notifications = request.json()
    notifications = notifications['data']
    return notifications

def getReplies(pageNumber):
    #
    # Returns a list of replies, both comment and content
    # Not fully implemented yet, requires Authentification
    replies = []
    for reply in getNotifications(pageNumber):
        if reply['notif_type_class'] == 'comment':
            replies.append(reply)
    return replies

def getNotificationKeys():
    #
    # Returns a list of all usable notification keys
    #
    # Not fully implemented yet, requires Authentification
    return getNotifications(1)[0].keys()

def getNewestPostID():
    #
    # Returns the id number of the newest post on the site
    #
    newest = 0
    request = requests.get('http://empeopled.com/feed?page=1&sortby=2', headers={'User-Agent': 'Chrome/18.0.1025.133'})
    feed = request.json()['data']['posts']
    for post in feed:
        try:
            if post['share_id'] > newest:
                newest = post['share_id']
        except Exception:
            pass
    return newest
