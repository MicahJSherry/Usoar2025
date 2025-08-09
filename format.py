import json
from pprint import pprint
from boolpoly import boolpoly


def int_keys(data):
    new_data = {}
    for k,v in data.items():
        new_data[int(k)] = v
    return new_data



def get_pow_2(data):
    m = max(data.keys())
    i = 2
    pow2 = {}
    while 2**i-1 <= m:
        pow2[2**i-1] = data[2**i-1]
        i +=1

    return pow2



def factor_string(fact):
    rep = ""
    eles = set(fact)
    
    
    for e in eles:
        multi = fact.count(e)
        rep = rep + f"({str(boolpoly(e))})"
        if multi>1:
            rep = rep+f"^{multi}"
    return rep   

def laTex_list(data):
    rep = ""

    for k, v in data.items():
        rep += "\\subsection*{" + str(k) +"$" + str(boolpoly(k))+ "$  } \n"
        rep += "\\begin{enumerate}\n"
        for f in v:
            rep += f"\\item ${factor_string(f)}$  {f}\n"
        rep += "\\end{enumerate}\n\n"
    return rep


def laTex_stats(data):
    rep = "\\begin{tabular}{|r|r|r|}\n"
    rep += "\\hline\n"
    rep += "$n$ & $2^n$ & \\# factorizations \\\\ \\hline\n"

    for n, v in enumerate(data.keys()):
        rep += f"{n+2} & {v} & {len(data[v])} \\\\ \\hline \n"
    
    rep += "\\end{tabular}"
    return rep
def fact_len_count(data):
    count = {}
    for k, v in data.items():
        count[k]= {}
        for f in v:
            
            n = len(f)
            cur = count[k].get(n, 0)
            cur +=1
            count[k][n] = cur
    pprint(count)
    return count


def more_laTex_stats(data,count, n):
    rep = "\\begin{tabular}{|"+"r|"*(n+2)+"}\n"
    rep += "\\hline\n"
    rep += "$n$ & $2^n$ & "
    for i in range(1, n):
        rep += " & {i}"
    rep += "\\\\ \\hline\n"

    for n, v in enumerate(data.keys()):
        rep += f"{n+2} & {v} &  \\\\ \\hline \n"
    
    rep += "\\end{tabular}"
    return rep 

def calc_ratios(data,offset_dict=None):
    if offset_dict is None:
            offset_dict = {}
    
    def _calc_curr(k):
        if type(data[k])== list:
            val = len(data[k])
        else:
            val = data[k]
        print(val)
        return  val - offset_dict.get(k, 0)
    
    ratios = []
    
    prev = 0  
    for k in sorted(data.keys()):
        
        
        curr = _calc_curr(k)
        if prev != 0:
            ratios.append(curr/prev)
        prev = curr         
    return ratios

def factorization_img(data, file="factorization.jpg"):
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = True

    keys = sorted(data.keys())
    n = [n+1 for n in range(len(keys))]
    values = [len(data[k]) if isinstance(data[k], list) else data[k] for k in keys]

    plt.figure(figsize=(10, 6))
    plt.plot(n, values, marker='o',)
    plt.xticks(n)
    plt.xlabel('n')
    plt.ylabel('Number of Factorizations')
    plt.title('Unique Factorizations of $f_n(x)$')
    plt.grid(True)
    plt.savefig(file)
    plt.close()

def ratio_img(values, file="ratio.jpg"):
    import matplotlib.pyplot as plt
    plt.rcParams['text.usetex'] = True
    n = [i+2 for i in range(len(values))]

    plt.figure(figsize=(10, 6))
    plt.plot(n, values, marker='o',)
    plt.xticks(n)
    plt.xlabel('n')
    plt.ylabel('Ratio')
    plt.title('Ratio of the Number of Factorizations of $f_n(x)$')
    plt.grid(True)
    plt.savefig(file)
    plt.close()


if __name__ == "__main__":
    with open('factors_of_16383.json', 'r') as f:
        data = json.load(f)
            
    data = int_keys(data)
    data = get_pow_2(data)
    #factorization_img(data)
    ratio_img(calc_ratios(data)[1:])
    

