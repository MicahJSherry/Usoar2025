from boolpoly import boolpoly

k = 5
xp1 = boolpoly(2**k+1)

dict_f_n = {2**n-1: 0 for n in range(1,15)}

for i in range(2**16):
    
    p = (xp1*boolpoly(i)).poly
    if p in dict_f_n.keys():
        dict_f_n[p] += 1
print([dict_f_n[p]for p in dict_f_n.keys()])    


# conjecture

fibb = [0, 1]
for _ in range(12):
    fibb.append(fibb[-1]+fibb[-2])
print(fibb)
N = 16
for n in range(N+1):
    q = n // k
    r = n %  k
    print((fibb[q+2]**r)*(fibb[q+1]**(k-r)))

