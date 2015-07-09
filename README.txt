Hello!

This is the Empeople.com Unofficial API or EmUAPI for short.
Right now functionality is limited, it can only call data from the site. I'm
planning on adding the ability to post data to the site, but that is a bit more
complicated to do. For now though, this will help you grab data from the site,
until an official api is created.

Without further adieu heres the limited documentation!


getAllTopics()
  This returns a list of all topic dictionaries
  Usage:
    import emuapi

    print(emuapi.getAllTopics()[0]['name'])

    Out: Welcome to Empeopled

getAllTopicKeys()
  This returns a list of all keys that can be used with an element that was
  returned from getAllTopics() the 'name' in the previous example was a key
  Usage:
    import emuapi

    print(emuapi.getAllTopicKeys())

    Out: "Too many things for me to put here, just print it yourself!"

getTopicSID(topic)
  This returns the sid (int) of a topic (string) that is passed in.
  Usage:
    import emuapi

    print(emuapi.getTopicSID('Technology'))

    Out: 368

getAllTopicNames()
  Returns a list of all names usable in getTopicSID()

getTopicFeed(topic, pageNumber)
  Returns a list of all posts on the pageNumber (int) of a topic (string)
  Usage:
    import emuapi

    print(emuapi.getTopicFeed('Technology', 1)[0]['title'])
    
    Out: Welcome to Empeopled

getFeedKeys()
  Returns a list of all keys that can be used to access info from the posts
  returned by getTopicFeed()
  Usage:
    Just print it. You've got this.
