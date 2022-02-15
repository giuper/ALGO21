from sol import kmajority

def calcolaKM(k,stream):
    x=kmajority(k)
    for a in stream:
        x.addElement(a)
        print("Aggiungo ",a)
        print("k-maggioranza: ",x.returnKMaj())

stream=[3, 1, 3, 2, 3, 3, 2, 2, 3, 2, 7, 2]

for k in range(2,5):
    print("k=",k)
    calcolaKM(k,stream)
    print()


