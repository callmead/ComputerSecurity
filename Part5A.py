from Crypto.PublicKey import RSA
import tools, sys

def match_message(public_key_path, ciphertext_path, message_space_path):
    # Reading message space file
    message_space = open(message_space_path).readlines()
    # Reading captured cipher
    cipher_message = open(ciphertext_path).read().strip()
    # Reading public key
    secret_public_key = RSA.importKey(open(public_key_path, 'r').read())
    # Reading and encrypting message space messages and comparing each with captured cipher
    counter = 1
    for line in message_space:
        secret_message = line.strip()
        secret_message_int = tools.text_to_int(secret_message)
        secret_ciphertext = secret_public_key.encrypt(secret_message_int, None)
        # print secret_ciphertext
        from collections import Counter
        if Counter(str(secret_ciphertext)) == Counter(str(cipher_message)):
            print '****************************************************'
            print 'Message '+str(counter)+' matched -> ' + line.strip()
            print 'Ciphertext: ' + str(secret_ciphertext)
            print '****************************************************'
        else:
            print 'Message '+str(counter)+' not matched!'
        counter += 1

if __name__ == "__main__":
    try:
        sys.argv[1]
    except IndexError:
        print 'Please provide public key path'
        quit()
    try:
        sys.argv[2]
    except IndexError:
        print 'Please provide captured ciphertext file path'
        quit()
    try:
        sys.argv[3]
    except IndexError:
        print 'Please provide message space file path'
        quit()
    match_message(sys.argv[1], sys.argv[2], sys.argv[3])
