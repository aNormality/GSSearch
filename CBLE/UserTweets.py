__author__ = 'AP'

class UserTweets(object):
    userTweetWords =  {
        'user1' : ['sweets','durga','nalanda','howrah','sweets'],
        'user2' : ['patna','lalu','nalanda','bhojpuri','sweets']
    }

    pWordCount = {}
    totWordCount = 0

    def buildWordDist(self):
        pWD={}
        for wl in self.userTweetWords.values():
            for w in wl:
                if pWD.has_key(w):
                    pWD[w] = pWD[w] + 1
                else:
                    pWD[w] = 1
        self.pWordCount = pWD
        self.totWordCount = sum(pWD.values())


    def wordPerc(self,w):

        if len(self.pWordCount)==0:
            self.buildWordDist()

        #print(self.pWordCount,self.totWordCount)
        if self.pWordCount.has_key(w):
            #print("found word " , w, self.pWordCount[w],self.totWordCount)
            return float(self.pWordCount[w]*100/self.totWordCount)
        else:
            return float(0.0)

#obj = UserTweets()
#print(obj.wordPerc("sweets"))
