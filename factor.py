
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


factor_map = {}
mf = 0b10000000000
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

pprint(uni)    
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
            irreducable.append(factorization)        

    for fact in factor_map[N]:
        _helper(N, fact)

    return irreducable


poly  = []
count = []
for N in factor_map.keys():
    x = irreduceable_factors(N, factor_map, uni)
    if len(x)>1:
        poly.append(N)
        count.append(len(x))
        print(x)
print(poly)
print(count)

"""x = int(input("enter number"))
while x > 0:
    pprint(factor_map[x])
    x = int(input("enter number"))
"""

#pprint(tree(mf-1, factor_map, uni))

import matplotlib.pyplot as plt
plt.plot(count)
plt.show()
