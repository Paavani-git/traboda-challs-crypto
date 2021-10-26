from sec import flag,key
pt1 = b"who_said_crypto_is_stressful?"
pt2 = flag
ct1,ct2 = "",""

def xorr(text,key): 
    return b''.join([bytes([key[i%len(key)]^j]) for i,j in enumerate(text)]) 
ct1 = xorr(pt1,key).decode()
ct2 = xorr(pt2,key).decode()

x = open("ciphertext.txt", "w")  
x.write(ct1 + "@@" + ct2)
x.close()
