from boolpoly import boolpoly

k = 3
xp1 = boolpoly(2**k+1)

dict_f_n = {2**n-1: 0 for n in range(1,15)}

for i in range(2**16):
    
    p = (xp1*boolpoly(i)).poly
    if p in dict_f_n.keys():
        dict_f_n[p] += 1
print([dict_f_n[p]for p in dict_f_n.keys()])    
