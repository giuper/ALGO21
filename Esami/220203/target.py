from back import BackTrack

class Target(BackTrack):

    def __init__(self,L,T):
        super().__init__()
        self.N=len(L)
        self.L=L
        self.T=T
        
    def isFinal(self,stato):
        [X,k]=stato
        sumP=0
        for i in range(k):
            sumP+=X[i]*self.L[i]
            
        return sumP==self.T

    def allMoves(self,stato):
        [X,k]=stato
        if k==self.N:
            return []
        else:
            return [0,1]

    def isAdm(self,stato,m):
        return True

    def newStato(self,stato,b):
        [X,k]=stato
        newStato=[]
        newStato.append(X.copy())
        newStato[0][k]=b
        newStato.append(k+1)
        return newStato

    def Solve(self,verbose=False):
        return self._Solve([[None]*self.N,0],verbose)

