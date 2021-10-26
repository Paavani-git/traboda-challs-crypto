from sec import flag,key

pt = flag
ct = ""

def byte_xor(text, key):  
     return bytes([b ^ ord(key) for b in text])  
                                                  
ct = byte_xor(flag,key) 
x = open("ciphertext.txt", "w")  
x.write(ct)
x.close()

