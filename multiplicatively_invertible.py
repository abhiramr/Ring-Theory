# MULTIPLICATIVE INVERSE

from commutative_rings_with_unity import *

def mult_invertible(set_, modulo):
    e = mul_iden(set_,modulo)
    if e is not None: 
        for i in range(1,len(set_)):
            yes = False
            for j in range(1,len(set_)):
                if multmod(set_[j],set_[i],modulo) == e:
                    yes = True
                    break
        if yes == False:
            print("Not every non-zero element has a multiplicative inverse")
        else:
            print("Every element has a multiplicative inverse")