from sol import TargetNC

def testCase(L,T):
    x=TargetNC(L,T)
    s=x.Solve()
    print("Lista: ",L)
    if s[0]:
        print("Ho trovato una soluzione per T=",T)
        for i in range(len(L)):
            if s[1][0][i]==1:
                print(f'{L[i]:3d} in posizione {i:2d}')
    else:
        print("Non ho trovato nessuna soluzione per T=",T)


L=[2,5,8,3,9,6]
for T in range(1,sum(L)):
    testCase(L,T)
    print()

