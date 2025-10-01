import string

CHARSET = string.printable[:-6]  # Exclude whitespace characters
N  = len(CHARSET)

def encrypt(plaintext, key):
    ciphertext = "" 
    key_length = len(key)
    for i, c in enumerate(plaintext):
        if c not in CHARSET:
            ciphertext += c
            continue
        p = CHARSET.index(c)
        k = CHARSET.index(key[i % key_length])
        c = CHARSET[(p + k) % N]
        ciphertext += c
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = "" 
    key_length = len(key)
    for i, c in enumerate(ciphertext):
        if c not in CHARSET:
            plaintext += c
            continue
        c = CHARSET.index(c)
        k = CHARSET.index(key[i % key_length])
        p = CHARSET[(c - k) % N]
        plaintext += p
    return plaintext

key = "LEMON"
plaintext = "ATTACKATDAWN"

ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Key:", key)
print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted: ", decrypted_text)