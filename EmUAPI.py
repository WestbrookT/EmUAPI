import json
import requests

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
