def Inverse(x,N):
    
    return ModExp(x, N - 2, N)
 
def ModExp(g,x,N):
 
    res = 1     

    while (x > 0) :
         
        if ((x & 1) == 1) :
            res = (res*g)%N
 
        # y must be even now
        x = x >> 1      # y = y/2
        g = (g*g)%N
         
    return res

def eGCD(a,b):

    if a == 0 :  
        return 0,1,b
             
    x,y,d = eGCD(b%a,a) 
     
    X = y - (b//a) * x
    Y = x 
     
    return (X,Y,d)


def enc(p,q,g,h,m,y):

    G = p*q

    gy = ModExp(g%p,y,p)

    hy = ModExp(h%p,y,p)
    hym = (hy*m)%p

    return (gy,hym)

def dec(p,q,x,ctxt):

    G = p*q
    c1,c2 = ctxt

    c1x = ModExp(c1%p,x,p)
    return (c2*Inverse(c1x,p))%p