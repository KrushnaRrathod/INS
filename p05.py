import numpy as np

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = modinv(det, modulus)
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    return matrix_mod_inv % modulus

def generate_key(key_string, n):
    key = [ord(char) - 65 for char in key_string.upper() if char.isalpha()]
    if len(key) != n**2:
        raise ValueError("Key length must be square of n")
    return np.array(key).reshape(n, n)

def prepare_input(text, n):
    text = text.upper().replace(' ', '')
    if len(text) % n != 0:
        text += 'X' * (n - (len(text) % n))
    return [ord(char) - 65 for char in text]

def hill_encrypt(plaintext, key):
    n = int(np.sqrt(len(key)))
    plaintext_matrix = np.array(prepare_input(plaintext, n)).reshape(-1, n)
    ciphertext_matrix = np.dot(plaintext_matrix, key) % 26
    return ''.join([chr(char + 65) for row in ciphertext_matrix for char in row])

def hill_decrypt(ciphertext, key):
    n = int(np.sqrt(len(key)))
    ciphertext_matrix = np.array(prepare_input(ciphertext, n)).reshape(-1, n)
    key_inverse = matrix_mod_inv(key, 26)
    plaintext_matrix = np.dot(ciphertext_matrix, key_inverse) % 26
    return ''.join([chr(char + 65) for row in plaintext_matrix for char in row])

# Example Usage
plaintext = "HELLO"
key_string = "GYBNQKURP"
key = generate_key(key_string, 3)
ciphertext = hill_encrypt(plaintext, key)
decrypted_text = hill_decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
