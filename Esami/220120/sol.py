def _maxInBitonic(A,s,f,verbose=False):

    if verbose:
        print("Searching maximum in bitonic list: ",A[s:f])

    if f==s+1: #la lista A[s:f] contiene un solo elemento
        return A[s]
    m=(s+f)//2

#nota che m>0
    if verbose:
        print("Value at the middle point: ",A[m])

    if m==len(A)-1: ##questo caso si verifica solo se s=len(A)-2 e f=len(A)
        if A[m]>A[m-1]:
            return A[m]
        else:
            return A[m-1]

#da questo punto in poi
#0<m<len(A)-1
        
    if A[m]>A[m-1] and A[m]>A[m+1]:
        return A[m]

    if A[m]>A[m-1] and A[m]<A[m+1]:
        return _maxInBitonic(A,m+1,f,verbose)

    if A[m]<A[m-1] and A[m]>A[m+1]:
        return _maxInBitonic(A,s,m,verbose)
        

def maxInBitonic(A,verbose=False):
    return _maxInBitonic(A,0,len(A),verbose)
        
