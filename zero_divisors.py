# Zero Divisors
def multmod(x,y,z):
    return (x*y)%z

def zero_divisors(set_,modulo):
    for i in range(1,len(set_)):
        yes = True
        for j in range(1,len(set_)):
            if multmod(set_[j],set_[i],modulo) == 0:
                yes = False
                break
        if yes == False:
            print("False for No Zero Divisors. Zero divisors exist so the given ring is not an integral domain")
            return
    if yes:
        print("True for No Zero Divisors. No zero divisors exist so the given ring is an Integral domain")
