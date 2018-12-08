__author__ = 'AP'

import math

class GeoFinder(object):

    err = 0.05
    xll=0
    xul=10
    yll=0
    yul=10
    alphaul=0
    alphall=1
    c=1

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

    def myFunc(self,geo,x,y,alpha):

        geo = self.wordGeoDist["sweets"]
        tot=0.0
        for g in geo.keys():
            d=math.sqrt((g[0]-x)**2 + (g[1]-y)**2)
            tot = tot + float(((self.c/math.pow(math.e,d*alpha))- geo[g])**2)

        return tot


    def initOptimize(self,geoWDist):

        iFixParam = 0
        x=0
        y=0
        alpha = 0.005
        totError = 100000

        while True:
            if iFixParam % 3 == 0:
                # Fix First , Second parameter , adjust third parameter
                x2=self.alphaul-((math.sqrt(5)-1)/2)*(self.alphaul-self.alphall)
                x1=self.alphall+((math.sqrt(5)-1)/2)*(self.alphaul-self.alphall)
                vret = self.optimize(geoWDist,0,x,y,alpha,self.alphall,x2,x1,self.alphaul)
                alpha=vret
            elif iFixParam % 3 == 1 :
                # Fix First , third parameter , adjust second parameter
                x2=self.yul-((math.sqrt(5)-1)/2)*(self.yul-self.yll)
                x1=self.yll+((math.sqrt(5)-1)/2)*(self.yul-self.yll)
                vret = self.optimize(geoWDist,1,x,y,alpha,self.yll,x2,x1,self.yul)
                y=vret
            else:
                # Fix second , third parameter , adjust first parameter
                x2=self.xul-((math.sqrt(5)-1)/2)*(self.xul-self.xll)
                x1=self.xll+((math.sqrt(5)-1)/2)*(self.xul-self.xll)
                vret = self.optimize(geoWDist,2,x,y,alpha,self.xll,x2,x1,self.xul)
                x=vret

            iFixParam = iFixParam + 1

            #print iFixParam

            if iFixParam%3==0:
                if abs(totError - self.myFunc(geoWDist,x,y,alpha)) > self.err:
                    totError = self.myFunc(geoWDist,x,y,alpha)
                else:
                    print(" x = ", x)
                    print(" y = ", y)
                    print(" alpha = ", alpha)
                    print(" Tot = ",self.myFunc(geoWDist,x,y,alpha))
                    break


    def optimize(self,geoWDist,iFixParam,x,y,alpha,ll,x2,x1,ul):

        if iFixParam==0:
            v2 = self.myFunc(geoWDist,x,y,x2)
            v1 = self.myFunc(geoWDist,x,y,x1)
        elif iFixParam==1:
            v2 = self.myFunc(geoWDist,x,x2,alpha)
            v1 = self.myFunc(geoWDist,x,x1,alpha)
        else:
            v2 = self.myFunc(geoWDist,x1,y,alpha)
            v1 = self.myFunc(geoWDist,x2,y,alpha)

        if abs(v2-v1) < self.err:
            return (x2+x1)/2

        if v2>v1 :
            ul=x1
            x1=x2
            x2=ul-((math.sqrt(5)-1)/2)*(ul-ll)
            ret = self.optimize(geoWDist,iFixParam,x,y,alpha,ll,x2,x1,ul)

        if v2<v1:
            ll=x2
            x2=x1
            x1=ll+((math.sqrt(5)-1)/2)*(ul-ll)
            ret = self.optimize(geoWDist,iFixParam,x,y,alpha,ll,x2,x1,ul)

        return ret

    def getWordCenters(self):

        for wGeo in self.wordGeoDist.keys():
            self.initOptimize(self.wordGeoDist[wGeo])

obj = GeoFinder()
#print(obj.myFunc(0,5,5,0.5))
obj.getWordCenters()
