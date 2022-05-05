import random



S1 = [0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf]
S2 = [0x5,0x6,0x7,0x8,0x9,0xa,0xb,0xc,0xd,0xe,0xf,0x0,0x1,0x2,0x3,0x4]
S3 = [0xa,0xb,0xc,0xd,0xe,0xf,0x0,0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9]
S4 = [0xe,0xf,0x0,0x1,0x2,0x3,0xa,0xb,0xc,0xd,0x4,0x5,0x6,0x7,0x8,0x9]



def gen():

    k = []

    for i in range(0,16):

        n = random.randint(0x00,0xFF)
        k.append(n)

    return k

def enc(k,ptxt):

    ka = k[:8]
    kb = k[8:]

    ctxt = []

    for i in range(0,8): 
        ctxt.append(ptxt[i])

    for i in range(0,8):
        ctxt[i]^=ka[i]

    for i in range(0,8):

        nib1 = ctxt[i]>>4
        nib2 = ctxt[i]&0b1111
    
        if i == 0 or i == 1:
            ctxt[i] = 16*S1[nib1]+S2[nib2]

        if i == 2 or i == 3:
            ctxt[i] = 16*S2[nib1]+S3[nib2]

        if i == 4 or i == 5:
            ctxt[i] = 16*S3[nib1]+S4[nib2]

        if i == 6 or i == 7:
            ctxt[i] = 16*S4[nib1]+S1[nib2]

    return ctxt

def dec(k,ctxt):

    ka = k[:8]
    kb = k[8:]

    ptxt = []
    
    for i in range(0,8): 
        ptxt.append(ctxt[i])

    for i in range(0,8):

        nib1 = ctxt[i]>>4
        nib2 = ctxt[i]&0b1111
        
        if i == 0 or i == 1:
            ctxt[i] = 16*S1.index(nib1)+S2.index(nib2)
   
        if i == 2 or i == 3:
            ctxt[i] = 16*S2.index(nib1)+S3.index(nib2)

        if i == 4 or i == 5:
            ctxt[i] = 16*S3.index(nib1)+S4.index(nib2)

        if i == 6 or i == 7:
            ctxt[i] = 16*S4.index(nib1)+S1.index(nib2)

    for i in range(0,8):
        ptxt[i]^=ka[i]



    return ptxt


k = gen()
msg = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

ctxt = enc(k,msg)
print(msg)
print(dec(k,ctxt))