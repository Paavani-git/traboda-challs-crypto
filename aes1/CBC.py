from Crypto.Cipher import AES 

from flag1 import plaintext

from Crypto.Util.Padding import *

import os 

flag=plaintext

key=b'Yellow submarine'

iv=os.urandom(16)

ct=AES.new(key,AES.MODE_CBC,iv).encrypt(pad(flag.encode(),16))

'''
ct=38ecc322be5384c20c1111d7391511c4d543c10e601b78fcc618dc735e59be2b
iv=240f9d273c3f5fc72b453cfd7e5e9311print(ct.hex())
'''
