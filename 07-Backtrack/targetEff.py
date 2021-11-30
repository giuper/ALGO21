from target import Target

class EffTarget(Target):

    def isFinal(self,stato):
        [X,k,S]=stato
        return S==self.T

    def allMoves(self,stato):
        [X,k,S]=stato
        if k==self.N or S>self.T:
            return []
        else:
            return [0,1]

    def newStato(self,stato,b):
        [X,k,S]=stato
        newStato=[]
        newStato.append(X.copy())
        newStato[0][k]=b
        newStato.append(k+1)
        newStato.append(S+b*self.L[k])
        return newStato

    def Solve(self,verbose=False):
        return self._Solve([[None]*self.N,0,0],verbose)


if __name__=='__main__':
    L=[2**i for i in range(20)]

    for T in range(2**20+1):
        q=Target(L,T)
        sol=q.Solve()
        if sol[0]:
            print(sol[1][0])
