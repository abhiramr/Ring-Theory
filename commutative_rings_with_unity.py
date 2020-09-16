def multmod(x,y,z):
    return (x*y)%z

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
