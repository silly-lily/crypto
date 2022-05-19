import util



def gen():

    p = 7 # any prime
    q = 2 # any prime

    N = p*q # secret key

    e = 5 # gcd(e,N) = 1 & 1 < e < phi(N)
    d = 11 # de = 1 (mod phi(N))

    return(N,e,d)


 
def encrypt(k,m):

    N,e,d = k

    return util.ModExp(m,e,N)



def decrypt(k,m):

    N,e,d = k

    return util.ModExp(m,d,N)