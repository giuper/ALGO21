
class Zaino:

    def __init__(self,W,V,B):
        self.W=W.copy()
        self.W.insert(0,None)
        self.V=V.copy()
        self.V.insert(0,None)
        self.B=B
        self.N=len(W)


    ##restituisce solo il valore massimo ottenibile
    ##ma non il sottoinsime che ottiene il massimo
    def Solve(self):
        N=self.N
        B=self.B
        
        T=[[None]*(B+1)]*(N+1)
        for i in range(0,N+1): #riempio colonna 0
            T[i][0]=0 #se lo zaino ha capacita' 0-->ottengo 0
        for b in range(0,B+1): #riempio riga 0
            T[0][b]=0 #se ho 0 oggetti --> ottengo 0
            
        for i in range(1,N+1):
            for b in range(1,B+1):
                print(f'riga={i} colonna={b}--->{T[i][b]}')
                if self.W[i]>b:
                    print(f'\tOggetto {i} troppo grande ({self.W[i]}) per zaino {b}')
                    T[i][b]=T[i-1][b]
                else:
                    print(f'\tOggetto {i} ({self.W[i]}) potrebbe entrare in zaino {b}')
                    print(f'\t\tentra    : {T[i-1][b-self.W[i]]+self.V[i]}')
                    print(f'\t\tnon entra: {T[i-1][b]}')
                    T[i][b]=max(T[i-1][b],T[i-1][b-self.W[i]]+self.V[i])
                print(f'riga={i} colonna={b}--->{T[i][b]}')
        return T[N][B]

W=[1,4,3]
V=[1500,3000,2000]
B=4

z=Zaino(W,V,B)
print("Massimo valore ottenibile=",z.Solve())
