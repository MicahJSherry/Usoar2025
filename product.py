from pprint import pprint
from boolpoly import boolpoly 

def product_table(highest_order):
    size = 0b1 << highest_order
    table  =[]
    for i in range(size):
        print(i)
        table.append([])
        for j in range(size):
            p = boolpoly(i) * boolpoly(j)
            table[i].append(p.poly)
    return table 

def get_irr(table, highest_order):
    N = 0b1<<highest_order
    irr = []
    for n in range(2,N):
        num_occ = 0 
        for row in table:
            num_occ += row.count(n)

        if num_occ <= 2:
            irr.append(n)
    return irr

table = product_table(12)
irr   = get_irr(table, 12)
pprint(irr)
print(len(irr))

def factor(f_x, table, irr):
    div = {}
    def _helper(g_x):
        div[g_x] = []
        for p_x in irr:
            for q_x, v in enumerate(table[p_x]): 
                if v == g_x and [q_x, p_x] not in div[g_x]:
                    div[g_x].append([min(p_x, q_x), max(p_x, q_x) ])
    
                    if q_x not in irr and q_x not in div.keys():    
                        _helper(q_x)
    _helper(f_x)
    pprint(div)
    
    
    factors = div[f_x]
    
    for k in sorted(div.keys() - {f_x}, key=int, reverse= True):
        print(k)
    
                
        for fact in factors[:]:
            
            if k in fact:
                factors.remove(fact)
                fact.remove(k)
                for k_fact in div[k]:
                    factors.append(k_fact+fact)
    final = []
    for fact in factors[:]:
        fact.sort()
        if fact not in final:
            final.append(fact)

        #print(k, factors)
    pprint(final)
    print(len(final))

    return final

factor(2**11-1, table, irr)
