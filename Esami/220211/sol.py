class kmajority:

    def __init__(self,k):
        self.elements={}
        self.k=k

    def addElement(self,a):
        currentElements=self.elements.keys()
        if a in currentElements:
            self.elements[a]+=1
            return
        if len(currentElements)<self.k-1:
            self.elements[a]=1
        else:
            tbd=[]
            for k in currentElements:
                self.elements[k]-=1
                if self.elements[k]==0:
                    tbd.append(k)
            for k in tbd:
                self.elements.pop(k)

    def returnKMaj(self):
        return list(self.elements.keys())

