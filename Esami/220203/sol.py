from target import Target

class TargetNC(Target):

    def allMoves(self,stato):
        [X,k]=stato
        if k==self.N:
            return []
        else:
            if X[k-1]==1:
                return [0]
            else:
                return [0,1]

