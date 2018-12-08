__author__ = 'AP'

import math

from WordLoc import WordLoc
from UserTweets import UserTweets

class CBLECore(object):


    LocDict = {
            'WB' : [15,10],
            'BIHAR':[20,30]
    }

    objWLoc = WordLoc()
    objUserTweets = UserTweets()

    def calcLocProb(self):
        for usr in self.objUserTweets.userTweetWords.keys():
            pCity = self.calcUserLocProb(self.objUserTweets.userTweetWords[usr])
            print(usr , pCity )


    def calcUserLocProb(self,usrWords):
        pCity={}
        for loc in self.LocDict.keys():
            #print (loc)
            pCity[loc]=0
            for w in usrWords:
                pwl= self.objWLoc.workLoc(w,loc)
                pwd=self.objUserTweets.wordPerc(w)
                pCity[loc] = pCity[loc] + pwl*pwd

        return pCity


    def distCoor(self,c1,c2):
        d = float(math.sqrt((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2))
        print(d)


    #distCoor(cityDict['kolkata'],cityDict['patna'])
