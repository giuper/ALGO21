from bloom import bloomF

#read words from FileW and returns a Bloom Filter with given parameters
def readingFile(FileW,m,k):
    BLOOM=bloomF(m,k)
    with open(FileW,'r') as f:
        for line in f:
            line=line.rstrip() #rimuovo il carattere di andata a capo
            BLOOM.insert(line)
    return BLOOM

#computes percentage of false positive from the words in FileW
def checkingFile(BLOOM,FileW):
    falsePos=0
    total=0
    with open(FileW,'r') as f:
        for line in f:
            line=line.rstrip() #rimuovo il carattere di andata a capo
            total+=1
            if BLOOM.lookup(line):
                falsePos+=1
    return falsePos/total

#constructs a Bloom filter with words from POS and returns the
#percentage of false positive from the words in NEG
def check(POS,NEG,m,k):
    BLOOM=readingFile(POS,m,k)
    return checkingFile(BLOOM,NEG)


file1="englishWords.txt"
numberOfWordsFile1=90000
file2="paroleItaliane.txt"
tolerance=.04

for k in range(3,14):
    for m in [x*.5 for x in range(4,20)]:
        fp=check(file1,file2,int(m*numberOfWordsFile1),k)
        #print(f"m={m:1.2f} {k:2d} {fp:1.3f}")
        if fp<tolerance:
            print(f'{"minima espansione per aver <"}{tolerance:1.2f}{" falsi negativi con "}{k:2d}{" hash function -->"}{m:3.1f}')
            break

