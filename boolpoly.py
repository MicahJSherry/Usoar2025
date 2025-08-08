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
