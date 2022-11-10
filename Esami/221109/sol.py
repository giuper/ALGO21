from bloom import bloomF


#leggo le parole in FileW a costruisco un Bloom Filter con parametri m,k
def readingFile(FileW,m,k):
    BLOOM=bloomF(m,k)
    with open(FileW,'r') as f:
        for line in f:
            line=line.rstrip() #rimuovo il carattere di andata a capo
            BLOOM.insert(line)
    return BLOOM

#costruisco la lista dei falsi positivi che si trovano in FileW
def checkingFile(BLOOM,FileW):
    res=[]
    with open(FileW,'r') as f:
        for line in f:
            line=line.rstrip() #rimuovo il carattere di andata a capo
            if BLOOM.lookup(line):
                res.append(line)
    return res

#tutto insieme: prima construisco da POS e poi controllo NEG
#POS file contenente le parole da immettere nel Bloom Filter
#NEG file contenente le parole da controllare se presenti
def check(POS,NEG,m,k):
    BLOOM=readingFile(POS,m,k)
    return checkingFile(BLOOM,NEG)


file1="englishWords.txt"
file2="paroleItaliane.txt"

mm=float(input("Inserire m: "))
m=int(mm*90000)

k=int(input("Inserire k: "))
fn=check(file1,file2,m,k)
print(fn)

