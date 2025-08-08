from format import int_keys, get_pow_2, calc_ratios
from boolpoly import boolpoly
import json

from pprint import pprint
from collections import Counter as bag
with open('factors_of_16383.json', 'r') as f:
    data = json.load(f)

data  = int_keys(data)
data  = get_pow_2(data)
count = {}
new   = {}
def diff_by_1(small, big):
    if len(small)+1 != len(big):
        return False
    b =  bag(big) - bag(small)
    
    return len(b)==1

for k in sorted(data.keys()):
    count[k]= 0
    new[k] = []
    #if k ==3:
    #    k_prev = k
    #    continue

    for f in data[k]:
        for k_prev in sorted(data.keys()):
            if k_prev > k or k_prev==3:
                continue
            for f_prev in data[k_prev]:
                
                if diff_by_1(f_prev,f):
                    new[k].append(f)
                    count[k] += 1
                    break
pprint(count)

pprint(calc_ratios(data,offset_dict=count))
pprint(new)