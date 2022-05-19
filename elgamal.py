import random
import util



def gen():

    q = 101 # any prime

    G = list(range(1,q))

    g = 1 # any number in {1,...,q-1} works since q is prime
    
    x = random.randint(1,q-1)
    h = util.ModExp(g,x)

    return (G,q,g,h)
    

    
def enc(p,q,g,h,m,y):

    gy = util.ModExp(g%p,y,p)

    hy = util.ModExp(h%p,y,p)
    hym = (hy*m)%p

    return (gy,hym)



def dec(p,q,x,ctxt):

    c1,c2 = ctxt

    c1x = util.ModExp(c1%p,x,p)

    m = (c2*util.Inverse(c1x,p))%p
    return m