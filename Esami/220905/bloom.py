import time
import hashlib
import random
import math
import sys

class bloomF:

    def __init__(self,m,k):
        self.M=m
        self.A=[0]*m
        self.H=[]
        for i in range(k):
            hh=hashlib.sha256()
            hh.update(str(random.randint(0,2**32-1)).encode())
            self.H.append(hh)


    def insert(self,x):
        xx=x.encode()
        for hh in self.H:
            hhh=hh.copy()
            hhh.update(xx)
            index=int(hhh.hexdigest(),16)%self.M
            self.A[index]=1

    def lookup(self,x):
        xx=x.encode()
        for hh in self.H:
            hhh=hh.copy()
            hhh.update(xx)
            index=int(hhh.hexdigest(),16)%self.M
            if self.A[index]==0:
                return False
        return True
    

