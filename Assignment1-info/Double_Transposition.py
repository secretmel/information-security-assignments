import math

def key_order(key: str):

    #return order as char index

    pairs = list(enumerate(key))
    pairs.sort(key=lambda x: (x[1], x[0]))
    return [p for p, _ in pairs]

def inverse_key_order(key: str):

    order = key_order(key)
    inverse = [0] * len(order)
    for i, o in enumerate(order):
        inverse[o] = i
    return inverse

def encrypt(plaintext: str, key: str) -> str:

    n = len(key)
    m = math.ceil(len(plaintext) / n)
    padded_length = n * m
    padded_plaintext = plaintext.ljust(padded_length, 'X')

    # Create the matrix
    matrix = [''] * n
    for i in range(padded_length):
        col = i % n
        matrix[col] += padded_plaintext[i]

    # Reorder columns based on key
    order = key_order(key)
    ciphertext = ''.join(matrix[i] for i in order)

    return ciphertext

def decrypt(ciphertext: str, key: str) -> str:

    n = len(key)
    m = len(ciphertext) // n

    # Create the matrix
    matrix = [''] * n
    order = key_order(key)
    for i in range(len(ciphertext)):
        col = order[i // m]
        matrix[col] += ciphertext[i]

    # Read the plaintext row-wise
    plaintext = ''.join(matrix[i][j] for j in range(m) for i in range(n))

    return plaintext.rstrip('X')

if __name__ == "__main__":
    key = "ZEBRAS"
    plaintext = "TRYTOCRACKTHIS"
    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted: {decrypted_text}")

