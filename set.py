from itertools import product, combinations
from random import randint
from pprint import pprint
from collections import Counter
from itertools import product
import json

def sum_prod(A, B):
    res = set()
    for a, b in product(A, B):
        res.add(a + b)
    return res
soln = []



def Sum(e,S):
    return {e + s for s in S}

def set_to_int(S):
    i = sum(0b1<<i for i in S)
    return i

def int_to_set(I):
    S = set()
    n = 0
    while I != 0:
        if (I & 1) == 1:
            S.add(n)
        n+=1
        I>>=1
    return S

def factor_set(T):
    valid = []
    def _factor(S, L, R):

        
        if sum_prod(L,R)==T:
            if (L,R) not in valid and (R,L) not in valid :
                valid.append((L,R))
            return 
        a = min(S)
        for m in range(a+1):
            Lc = L.copy()
            Rc = R.copy()
            if len(L) == 0 or (Sum(m, Rc).issubset(T) and Sum(a-m, Lc).issubset(T)): 
                Lc.add(m)
                Rc.add(a-m)
                _factor(S.copy()-{a},Lc, Rc)

    _factor(
        T.copy(),
        set(),
        set())
    return valid



class memoized_factors():
    def __init__(self):
        self.memo = []
    
    def index_memo(self, T):
        for i, p  in enumerate(self.memo):
            if p[0] == T:
                return i 
        return -1
    
    def append(self, S):
        f = factor_set(S)
        self.memo.append((S, f))
        return f
    def populate_memo(self, S ):
        if self.index_memo(S)!=-1:
            return
        factors = self.append(S)  
        
        for A, B in factors:
            
            if A != {0} and B != {0}:
                if self.index_memo(A) == -1:
                    self.populate_memo(A)

                if self.index_memo(B) == -1:
                    self.populate_memo(B)

memo = memoized_factors()    

F = {i for i in range(14)}
memo.populate_memo(F)

pprint(memo.memo)

factor = {}

for A, S in memo.memo:
    a = set_to_int(A)
    factor[a] = []
    if len(S)==1:
        factor[a].append([a])
    for L,R in S:
        if R != {0} and L != {0}:
            factor[a].append([set_to_int(L), set_to_int(R)])

def reduce(factor_tree):
    final = {}
    keys = set(factor_tree.keys()) 
    while len(keys) !=0:
        key = min(keys)
        
        factors = factor_tree[key]
        final[key] = []
        for f in factors:
            if len(f)==2:
                l=f[0]
                r=f[1]
                
                for L in final[l]:
                    for R  in final[r]:
                        #pprint(final)
                        print(L, R)  
                        F = (L+R)
                        F.sort()
                        if F not in final[key]:
                            final[key].append(F)
            else:
                final[key] = factor_tree[key]

        keys = keys - {key}
    pprint(factor_tree)
    print()
        
    return final

reduced = reduce(factor)

file_path_json = f'factors_of_{set_to_int(F)}.json'
with open(file_path_json, 'w') as json_file:
    json.dump(reduced, json_file, indent=4)

