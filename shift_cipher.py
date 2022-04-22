import random



''' Encryption where each plaintext hexadecimal
number is shifted up by key k (mod 0xFF). '''



''' Chooses a key between 0x00 and 0xFF. Returns
key k. '''
def gen():

    key = random.randint(0x00,0xFF)
    return key



''' Encrypts plaintext ptxt with key k. Returns
ciphertext ctxt. '''
def enc(k,ptxt):

    ctxt = []
    
    for i in range(0,len(ptxt)):

        ctxt.append(ptxt[i]^k)

    return ctxt



''' Decrypts ciphertext ctxt with key k. Returns
plaintext ptxt '''
def dec(k,ctxt):
    
    ptxt = []
    
    for i in range(0,len(ctxt)):
        
        ptxt.append(ptxt[i]^k)

    return ptxt
