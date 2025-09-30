import string

# character set
CHARSET = string.printable[:-6]
N = len(CHARSET)
print(f"Charset size: {N}")

def shift_char(c, k, encrypt=True):
    if c not in CHARSET:
        return c
    idx = CHARSET.index(c)
    if encrypt:
        new_idx = (idx + k) % N
    else:  # decrypt
        new_idx = (idx - k) % N
    return CHARSET[new_idx]

#encrypt and decrypt functions
def caesar_extended_encrypt(plaintext, key):
    ciphertext = ""
    key_len = len(key)
    for i, c in enumerate(plaintext):
        k = key[i % key_len]   # numeric key
        ciphertext += shift_char(c, k, encrypt=True)
    return ciphertext

def caesar_extended_decrypt(ciphertext, key):
    plaintext = ""
    key_len = len(key)
    for i, c in enumerate(ciphertext):
        k = key[i % key_len]
        plaintext += shift_char(c, k, encrypt=False)
    return plaintext

# Example
key = [3, 3, 1, 5, 6]  
plaintext = "Hello World!!!"

ciphertext = caesar_extended_encrypt(plaintext, key)
decrypted = caesar_extended_decrypt(ciphertext, key)

print("Plaintext :", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)
