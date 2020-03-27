#pip install pycrypto Padding pillow
# Library modules you may need
from Crypto.Cipher import AES
from Crypto import Random
import hashlib, sys, binascii, Padding, random

def encrypt(plaintext, key, mode, iv):
    #Mode 1 ECB, Mode 2 CBC
    if mode == 1:
        print 'Selected mode:', mode, '- ECB'
        encobj = AES.new(key, mode)
        return(encobj.encrypt(plaintext))
    elif mode==2:
        print 'Selected mode:', mode, '- CBC'
        encobj = AES.new(key, mode, iv)
        return (encobj.encrypt(plaintext))
    else:
        print 'Mode not recognized.'
        return ''

# Part 1.A - Setup
#Open the image file and read lines
f = open('tux.ppm')
lines = f.readlines()
#seperate header from the body
header_data = lines[0] + lines[1] + lines[2]
body_data = lines[3]
#secret key
key='secretkey'
key = hashlib.sha256(key).digest()
#--------------------------------------------------------------------------------------

# Part 1.A - ECB
# The plain text after padding
plaintext = Padding.appendPadding(body_data, blocksize = Padding.AES_blocksize, mode=0)
# Encryption
ciphertext = encrypt(plaintext, key, AES.MODE_ECB, '')
# Prepending header_data back to the encrypted data
new_file = header_data+ciphertext
with open('ECB_tux.ppm', 'wb') as outf:
    outf.write(new_file)
#--------------------------------------------------------------------------------------

# Part 1.A - CBC
iv=100
iv= hex(iv)[2:8].zfill(16)
# The plain text after padding
plaintext = Padding.appendPadding(body_data,blocksize=Padding.AES_blocksize,mode=0)
# Encryption
ciphertext = encrypt(plaintext, key, AES.MODE_CBC, iv)
# Prepending header_data back to the encrypted data
new_file = header_data+ciphertext
with open('CBC_tux.ppm', 'wb') as outf:
    outf.write(new_file)
#--------------------------------------------------------------------------------------
