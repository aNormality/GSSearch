__author__ = 'AP'

class WordLoc(object):

    pWordLoc = {
        'sweets' : {
            'WB' : 0.5,
            'BIHAR' : 0.2
        },
        'durga' : {
            'WB' : 0.8,
            'BIHAR' : 0.30
        }
        ,
        'nalanda' : {
            'WB' : 0.2,
            'BIHAR' : 0.90
        }
        ,
        'lalu' : {
            'WB' : 0.2,
            'BIHAR' : 0.80
        }
        ,
        'patna' : {
            'WB' : 0.2,
            'BIHAR' : 0.80
        }
        ,
        'bhojpuri' : {
            'WB' : 0.2,
            'BIHAR' : 0.80
        }
    }


    def workLoc(self,w,loc):
        if self.pWordLoc.has_key(w):
            return (self.pWordLoc[w])[loc]
        else:
            return 0.0
