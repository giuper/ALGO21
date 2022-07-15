from bloom import bloomF


def readingFile(nomeFile,m,k):
    BLOOM=bloomF(m,k)
    with open(nomeFile,'r') as f:
        for line in f:
            line=line.rstrip() #rimuovo il carattere di andata a capo
            BLOOM.insert(line)
    return BLOOM

def checkingFile(BLOOM,name):
    false=0
    total=0
    with open(name,'r') as f:
        for line in f:
            line=line.rstrip() #rimuovo il carattere di andata a capo
            total+=1
            if BLOOM.lookup(line):
                false+=1
    return false/total


for m in range(2,8):
    mE=1.1
    mI=1.1
    kE=None
    kI=None
    for k in range(2,9):
        #costruisco il Bloom Filter per le parole inglesi
        BLOOM=readingFile("inglesiPos.txt",m*45_000,k)
        #calcolo la percentuale di falsi negativi per le parole inglesi
        fp=checkingFile(BLOOM,"inglesiNeg.txt")
        if fp<mE:
            mE=fp
            kE=k
        
        #costruisco il Bloom Filter per le parole italiane
        BLOOM=readingFile("italianePos.txt",m*140_000,k)
        #calcolo la percentuale di falsi negativi per le parole italiane
        fp=checkingFile(BLOOM,"italianeNeg.txt")
        if fp<mI:
            mI=fp
            kI=k

    print(f'{"Inglese:":12s}{"m: "}{m:1.2f}{"  k: "}{kE:d}')
    print(f'{"Italiano:":12s}{"m: "}{m:1.2f}{"  k: "}{kI:d}')
            
