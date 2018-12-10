__author__ = 'AP'

from GeoCoordinateFinder import GeoCoordinateFinder
import math

class TweetCore(object):

    objGeoFinder = GeoCoordinateFinder()

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
        (18,5) : {'nalanda':0,'durga':2,'howrah':2},
        (16,5) : {'nalanda':0,'durga':2,'howrah':3},
        (14,5) : {'nalanda':5,'durga':2,'howrah':10},
        (12,5) : {'nalanda':10,'durga':2,'howrah':41},
        (10,5) : {'nalanda':50,'durga':2,'howrah':13},
        (8,5) : {'nalanda':10,'durga':2,'howrah':6},
        (6,5) : {'nalanda':3,'durga':12,'howrah':6},
        (5,5) : {'nalanda':0,'durga':25,'howrah':6},
        (4,5) : {'nalanda':0,'durga':12,'howrah':5},
        (2,5) : {'nalanda':0,'durga':2,'howrah':3},
        (0,5) : {'nalanda':0,'durga':2,'howrah':1}
    }


    def wordGeoDistribution(self):
        wGDist={}
        ltr={}

        for loc in self.locWordListPP.keys():
            wl=self.locWordListPP[loc]
            for w in wl.keys():
                wc=wl[w]
                if wGDist.has_key(w):
                    ltr = wGDist[w]
                    if ltr.has_key(loc):
                        v=ltr[loc]
                        ltr[loc] = v + wc
                    else:
                        ltr[loc] = wc
                else:
                    wGDist[w] = {}
                    (wGDist[w])[loc] = wc

        #print wGDist
        self.tweetGeoLocator(wGDist)

    def tweetGeoLocator(self,wGeoDist):
        self.objGeoFinder.getWordCenters(wGeoDist)


obj = TweetCore()
obj.wordGeoDistribution()

#print(math.log(4792154.84073,math.e))
#print(math.log(3637278.91725,math.e))
#print(math.log(1589873.12627,math.e))
