__author__ = '118618'

import math


class MultiGS(object):

    err = 0.05
    x1ll=0
    x1ul=3
    x2ll=0
    x2ul=math.pi/2

    def myFunc(self,x1,x2):
        ret = float((6-2*x1+x1*math.cos(x2))*x1*math.sin(x2))
        return ret


    def intiOptimize(self):

        iFixParam = 0
        p1=0
        p2=math.pi/6

        while iFixParam < 10:
            if iFixParam % 2 == 0:
                # Fix First parameter , adjust Second parameter
                x2=self.x2ul-((math.sqrt(5)-1)/2)*(self.x2ul-self.x2ll)
                x1=self.x2ll+((math.sqrt(5)-1)/2)*(self.x2ul-self.x2ll)
                vret = self.optimize(0,p1,p2,self.x2ll,x2,x1,self.x2ul)
                p2=vret
            else:
                # Fix Second parameter , adjust First parameter
                x2=self.x1ul-((math.sqrt(5)-1)/2)*(self.x1ul-self.x1ll)
                x1=self.x1ll+((math.sqrt(5)-1)/2)*(self.x1ul-self.x1ll)
                vret = self.optimize(1,p1,p2,self.x1ll,x2,x1,self.x1ul)
                p1=vret

            iFixParam = iFixParam + 1
            print(" p1 = ", p1)
            print(" p2 = ", p2)
            print(" Value = ",self.myFunc(p1,p2))




    def optimize(self,iFixParam,p1,p2,ll,x2,x1,ul):

        if iFixParam==0:
            v2 = self.myFunc(p1,x2)
            v1 = self.myFunc(p1,x1)
        else:
            v2 = self.myFunc(x2,p2)
            v1 = self.myFunc(x1,p2)


        if abs(v2-v1) < self.err:
            print("Optimum value found at ", (x2+x1)/2)
            return (x2+x1)/2

        if v2>v1 :
            ul=x1
            x1=x2
            x2=ul-((math.sqrt(5)-1)/2)*(ul-ll)
            ret = self.optimize(iFixParam,p1,p2,ll,x2,x1,ul)

        if v2<v1:
            ll=x2
            x2=x1
            x1=ll+((math.sqrt(5)-1)/2)*(ul-ll)
            ret = self.optimize(iFixParam,p1,p2,ll,x2,x1,ul)


        return ret
