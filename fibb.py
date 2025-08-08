from boolpoly import boolpoly


xp1 = boolpoly(3)

for n in range(3,14):
    count = 0
    for g_x in range(2**(n-1), 2**(n)):
        if  (xp1*boolpoly(g_x)).poly== 2**(n+1)-1:
            count +=1 

    print(n,boolpoly(2**(n)-1), count)