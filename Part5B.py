import tools, sys

def extract_message(ciphertext_path):
    cipher_message = open(ciphertext_path).read().strip()
    print 'Message in ciphertext ->', tools.int_to_text(tools.find_root(int(cipher_message[1:-3]), 3))

if __name__ == "__main__":
    try:
        sys.argv[1]
    except IndexError:
        print 'Please provide the ciphertext file path'
        quit()
    extract_message(sys.argv[1])
