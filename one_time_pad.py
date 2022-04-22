import math
import random



''' Encryption where each plaintext hexadecimal
number is shifted up by key k (mod 0xFF) in
cycles. The ith position of ptxt is shifted by the 
ith position of the key. '''



''' Chooses a keylength keylen between 1 and N. Then 
chooses keylen amount of hexadecimal numbers to fill
in the key'''
def gen(N):

    key = []

    keylen = random.randint(1,N)
    for i in range(0,keylen):

        n = random.randint(0x00,0xFF)
        key.append(n)

    return key



''' Encrypts plaintext ptxt with key k. Returns
ciphertext ctxt. '''
def enc(k,ptxt):

    ctxt = []

    for i in range(0,len(ptxt)):

        n = ptxt[i]^k[i%len(k)]
        ctxt.append(n)

    return ctxt



''' Decrypts ciphertext ctxt with key k. Returns
plaintext ptxt. '''
def dec(k,ctxt):

    ptxt = []

    for i in range(0,len(ctxt)):

        n = ctxt[i]^k[i%len(k)]
        ptxt.append(n)

    return ptxt