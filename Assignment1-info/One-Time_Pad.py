import string, random

# Character set
CHARSET = string.printable[:-6]
N = len(CHARSET)

def otp_encrypt(plaintext):
    key = ''.join(random.choice(CHARSET) for _ in range(len(plaintext)))
    ciphertext = ""
    for p, k in zip(plaintext, key):
        p_idx = CHARSET.index(p)
        k_idx = CHARSET.index(k)
        c_idx = (p_idx + k_idx) % N
        ciphertext += CHARSET[c_idx]
    return ciphertext, key

def otp_decrypt(ciphertext, key):
    plaintext = ""
    for c, k in zip(ciphertext, key):
        c_idx = CHARSET.index(c)
        k_idx = CHARSET.index(k)
        p_idx = (c_idx - k_idx) % N
        plaintext += CHARSET[p_idx]
    return plaintext

# Example
plaintext = "HELLO"
ciphertext, key = otp_encrypt(plaintext)
decrypted = otp_decrypt(ciphertext, key)

print("Plaintext :", plaintext)
print("Key       :", key)
print("Ciphertext:", ciphertext)
print("Decrypted :", decrypted)
