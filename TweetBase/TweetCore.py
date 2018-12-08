__author__ = 'AP'

class TweetCore(object):

    userTweetBase = {
        'user1' : {
            'loc': {'x':10,'y':20},
            'tweets': ['this is first tweet for sweets','hello durga pujo','this is kolkata ','howrah bridge']
        },
        'user2' : {
            'loc': {'x':30,'y':40},
            'tweets': ['this is patna','hello lalu','this is nalanda','bhojpuri songs']
        }
    }

    #words used per person at a geo location
    locWordListPP = {
        (5,5) : {'sweets':20,'durga':25,'howrah':32},
        (4,5) : {'sweets':8,'durga':12,'howrah':12},
        (2,5) : {'sweets':5,'durga':2,'howrah':3},
        (0,5) : {'sweets':0,'durga':2,'howrah':1},
        (6,5) : {'sweets':8,'durga':12,'howrah':12},
        (8,5) : {'sweets':5,'durga':2,'howrah':3},
        (10,5) : {'sweets':0,'durga':2,'howrah':1},
    }

    wordGeoDist = {
        'sweets' : {
            (5,0) : .20,
            (4,0) : .08,
            (2,0) : .05,
            (0,0) : 0,
            (6,0) : .08,
            (8,0) : .05,
            (10,0) : 0
        }
    }


obj = TweetCore()
for w in obj.wordGeoDist.keys():
    for item in obj.wordGeoDist[w]:
        print item
