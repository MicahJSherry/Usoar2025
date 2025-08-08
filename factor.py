def int_to_set(I):
    S = set()
    n = 0
    while I != 0:
        if (I & 1) == 1:
            S.add(n)
        n+=1
        I>>=1
    return S

class boolpoly:
    def __init__(self, poly):
        self.poly = poly
    
    def __add__(self, other):
        return boolpoly(self.poly | other.poly)

    def __mul__(self, other):
        M = self.poly
        N = other.poly
        p = 0
        while N != 0: 
            p |= ((N & 1) * M) # (p or M) if LSB(N) = 1
            M <<= 1  
            N >>= 1  

        return boolpoly(p) 
    def __eq__(self, other):
        if type(self) == type(other):
            self.poly == other.poly
        return self.poly == other
    def __str__(self):
        temp = self.poly
        rep = str(temp&1) 
        temp >>=1 
        low = 1 
        while temp != 0:            
            lsb = temp & 1
            temp >>= 1
            if lsb==1:
                rep = "x^"+str(low)+" + "+rep
            low += 1
        return rep

def product(l):
    p = boolpoly(1)
    for e in l: 
        p *= boolpoly(e)
    return p



factor_map = {}
mf = 0b1 << 8
print(mf)
for i in range(1, mf):
    x = boolpoly(i)
    for j in range(1, mf):
        y = boolpoly(j)
        p = x*y
        if p.poly >=mf:
            continue
        factor_list = factor_map.get(p.poly, [])
        
        if (x.poly == p.poly or y.poly == p.poly):
            if [p.poly] not in factor_list:
                factor_list.append([p.poly])
        elif [y.poly, x.poly] not in factor_list:
            factor_list.append([x.poly, y.poly])
        factor_map[p.poly] = factor_list

from pprint import pprint

uni   = []
for N in factor_map:
    if len(factor_map[N])==1:
        uni.append(N)
for u in uni:
    print(f"{u}")#,     {str(boolpoly(u)):>40},     {int_to_set(u)}" ) 

exit()
def irreduceable_factors(N, factor_map, unique):
    irreducable = []
    def _helper(n, factorization):
        irr = True
        factorization = factorization.copy()
        factorization.sort()

        for f in factorization:
            if f not in unique and (f != n):
                irr = False
                factorization.remove(f)
                for option in factor_map[f]:
                    if option != [f]:
                        _helper(n, factorization+option)
        if irr and factorization not in irreducable:
            if product(factorization) == N:
                irreducable.append(factorization)        
    for fact in factor_map[N]:
        _helper(N, fact)
    if len(irreducable)>1:
        irreducable.remove([N])
    return irreducable

def factor_string(fact):
    rep = ""
    eles = set(fact)
    
    
    for e in eles:
        multi = fact.count(e)
        rep = rep + f"({str(boolpoly(e))})"
        if multi>1:
            rep = rep+f"^{multi}"
    return rep        
i = 1
pow2minus1 = []
while 2 ** i - 1< mf >> 1:
    pow2minus1.append(2**i-1)
    i += 1
poly  = []
count = []
num_irr = {}
for N in pow2minus1: #factor_map.keys():
    x = irreduceable_factors(N, factor_map, uni)
    poly.append(str(boolpoly(N)))
    count.append(len([i for i in x if 3 not in i]))
    print(N)
    num_irr[N] = {}
    for fact in x:
        if 3 not in fact:
            num_irr[N][len(fact)]= num_irr[N].get(len(fact),0)+1
            print(f"\item ${factor_string(fact)}$ {fact}")
    print()
print(poly)
print(count)
print()
pprint(num_irr)
exit()
"""
x = int(input("enter number"))
while x > 0:
    pprint(factor_map[x])
    x = int(input("enter number"))
"""

#pprint(tree(mf-1, factor_map, uni))

import matplotlib.pyplot as plt
plt.plot(count)
plt.show()
