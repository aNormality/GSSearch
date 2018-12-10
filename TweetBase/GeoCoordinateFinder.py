__author__ = 'AP'

import math

class GeoCoordinateFinder(object):

    err = 0.05
    xll=0
    xul=0
    yll=0
    yul=0
    sd=0.5

    def normalValue(self,mean,sd,pv):
        p = math.pow(math.e,-1*math.pow(pv-mean,2)/(2*sd*sd))/(sd*math.sqrt(2*math.pi))

        return p


    def myFunc(self,ptype,geo,xy,sd):

        tot=0.0

        glen = len(geo)
        nd=0.0

        for g in geo.keys():
            if ptype == 2:
                nd = self.normalValue(xy,sd,g[1])
            elif ptype == 1:
                nd = self.normalValue(xy,sd,g[0])

            tot = tot + math.pow((nd-geo[g])*100,2)

        tot = tot/glen
        #print(tot)
        return -1*tot


    def minXCoordinate(self,geo):
        imin=0
        for g in geo.keys():
            if imin>g[0]:
                imin=g[0]

        return imin

    def minYCoordinate(self,geo):
        imin=0
        for g in geo.keys():
            if imin>g[1]:
                imin=g[1]

        return imin

    def maxXCoordinate(self,geo):
        imax=0
        for g in geo.keys():
            if imax<g[0]:
                imax=g[0]

        return imax

    def maxYCoordinate(self,geo):
        imax=0
        for g in geo.keys():
            if imax<g[1]:
                imax=g[1]

        return imax

    def initOptimize(self,geoWDist):

        iFixParam = 0
        xmean=self.minXCoordinate(geoWDist)
        ymean=self.minYCoordinate(geoWDist)
        self.xll=self.minXCoordinate(geoWDist)
        self.xul=self.maxXCoordinate(geoWDist)
        self.yll=self.minYCoordinate(geoWDist)
        self.yul=self.maxYCoordinate(geoWDist)

        totError = 100000

        while iFixParam<100:
            # Fix First , third parameter , adjust second parameter
            x2=self.yul-((math.sqrt(5)-1)/2)*(self.yul-self.yll)
            x1=self.yll+((math.sqrt(5)-1)/2)*(self.yul-self.yll)
            ymean = self.optimize(geoWDist,2,ymean,self.sd,self.yll,x2,x1,self.yul)

            x2=self.xul-((math.sqrt(5)-1)/2)*(self.xul-self.xll)
            x1=self.xll+((math.sqrt(5)-1)/2)*(self.xul-self.xll)
            xmean = self.optimize(geoWDist,1,xmean,self.sd,self.xll,x2,x1,self.xul)

            iFixParam = iFixParam + 1

        retValue = {'x':xmean,'y':ymean}

        return retValue


    def optimize(self,geoWDist,ptype,xymean,sd,ll,x2,x1,ul):

        v2 = self.myFunc(ptype,geoWDist,x2,sd)
        v1 = self.myFunc(ptype,geoWDist,x1,sd)

        if abs(v2-v1) < self.err:
            return (x2+x1)/2

        if v2>v1 :
            ul=x1
            x1=x2
            x2=ul-((math.sqrt(5)-1)/2)*(ul-ll)
            ret = self.optimize(geoWDist,ptype,xymean,sd,ll,x2,x1,ul)

        if v2<v1:
            ll=x2
            x2=x1
            x1=ll+((math.sqrt(5)-1)/2)*(ul-ll)
            ret = self.optimize(geoWDist,ptype,xymean,sd,ll,x2,x1,ul)

        return ret


    def getWordCenters(self,wordGeoDist):
        for wGeo in wordGeoDist.keys():
            #print(wordGeoDist[wGeo])
            ret = self.initOptimize(wordGeoDist[wGeo])
            print(wGeo,'x=',ret['x'],'y=',ret['y'])
            print(self.myFunc(1,wordGeoDist[wGeo],ret['x'],self.sd)+self.myFunc(2,wordGeoDist[wGeo],ret['y'],self.sd))


# def myFunc(ptype,geo,xy,sd):

#obj = GeoFinder()
#print(obj.myFunc(1,0,30.9016994375,0.025))
#print(obj.myFunc(1,0,19.0983005625,0.025))
#print(obj.myFunc(2,0,6,0.025))
#print(obj.myFunc(2,0,10,0.025))
#print(obj.myFunc(2,0,0,0.025))
#obj.getWordCenters()
