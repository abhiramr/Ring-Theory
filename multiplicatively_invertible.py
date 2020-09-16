# MULTIPLICATIVE INVERSE

def mul_iden(set_ , modulo):
    for i in range(0,len(set_)):
        yes = True
        for j in range(0,len(set_)):
            if multmod(set_[j],set_[i],modulo)!=set_[j]:
                yes = False
                break
        if yes:
            iden = set_[i]
            print("Unity = {}".format(iden))
            return iden
    print("No Inverse")
    return None

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
