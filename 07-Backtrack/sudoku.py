puzzle=[
[None,4,None,None,None,None,1,7,9],
[None,None,2,None,None,8,None,5,4],
[None,None,6,None,None,5,None,None,8],
[None,8,None,None,7,None,9,1,None],
[None,5,None,None,9,None,None,3,None],
[None,1,9,None,6,None,None,4,None],
[3,None,None,4,None,None,7,None,None],
[5,7,None,1,None,None,2,None,None],
[9,2,8,None,None,None,None,6,None]
]

from back import BackTrack

class Sudoku(BackTrack):

    def __init__(self,puzzle):
        self.P=[puzzle[i].copy() for i in range(9)]
        
    def isFinal(self,stato):
        M,row,col=stato
        return row==9

    def allMoves(self,stato):
        M,row,col=stato
        if M[row][col] is None:
            return range(1,10)
        else:
            return [M[row][col]]

    def newStato(self,stato,m):
        M,row,col=stato

        #non basta fare newM=M.copy()
        #newM=M non funziona
        #newM=M.copy() nemmeno
        #in generale usa deepcopy
        #qui non c'e' bisogno perche' abbiamo solo due livelli
        newM=[M[i].copy() for i in range(9)]
        if col==8:
            row+=1
            col=0
        else:
            col+=1
        newM[row][col]=m
        newstato=[newM,row,col]
        return newstato

    def isAdm(self,stato,m):
        M,row,col=stato

        if M[row][col]==m:
            return True
        
        #controlla riga row
        for c in range(9):
            if M[row][c]==m:
                return False
            
        #controlla colonna col
        for r in range(9):
            if M[r][col]==m:
                return False

        #controlla riquadro
        ##coordinate della cella in alto a sinistra
        ##del riquadro cui appartiene (row,col)
        cornerR=(row//3)*3
        cornerC=(col//3)*3
        for r in range(cornerR,cornerR+3):
            for c in range(cornerC,cornerC+3):
                if M[r][c]==m:
                    return False

        return True

            
    def Solve(self):
        res=self._Solve([self.P,0,0])
        if res[0]:
            print("Trovata soluzione")
            print(res[1])
        else:
            print("Nessuna soluzione")

sudoku=Sudoku(puzzle)
sudoku.Solve()
