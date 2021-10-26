from Crypto.Cipher import AES 

from flag import plaintext

from Crypto.Util.Padding import *

flag=plaintext

key=b'Yellow submarine'

ct=AES.new(key,AES.MODE_ECB).encrypt(pad(flag.encode(),16))

#ct=d6d028810212d6241e74024e0b1db4a22a593aa717e08580340f3f4b57f36b74