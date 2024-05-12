# Initial Permutation Table
IP = [2, 6, 3, 1, 4, 8, 5, 7]

# Final Permutation Table
FP = [4, 1, 3, 5, 7, 2, 8, 6]

# Expansion Permutation Table
EP = [4, 1, 2, 3, 2, 3, 4, 1]

# P-Box Permutation Table
P = [2, 4, 3, 1]

# S-Box Tables
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]

def permute(original, table):
    return [original[i - 1] for i in table]

def generate_keys(key):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]

    key = permute(key, P10)
    left_half = key[:5]
    right_half = key[5:]

    left_half = left_half[1:] + left_half[:1]
    right_half = right_half[1:] + right_half[:1]

    key1 = permute(left_half + right_half, P8)

    left_half = left_half[2:] + left_half[:2]
    right_half = right_half[2:] + right_half[:2]

    key2 = permute(left_half + right_half, P8)

    return key1, key2

def Fk(key, right_half):
    right_half = permute(right_half, EP)

    right_half = [int(right_half[i]) ^ int(key[i]) for i in range(len(key))]

    row = int(''.join(map(str, [right_half[0], right_half[3]])), 2)
    col = int(''.join(map(str, right_half[1:3])), 2)
    value = S0[row][col]

    row = int(''.join(map(str, [right_half[4], right_half[7]])), 2)
    col = int(''.join(map(str, right_half[5:7])), 2)
    value = value * 4 + S1[row][col]

    value = format(value, '02b')
    value = permute(list(map(int, value)), P)

    return value

def encrypt(plain_text, key):
    key1, key2 = generate_keys(key)
    plain_text = permute(plain_text, IP)

    left_half = plain_text[:4]
    right_half = plain_text[4:]

    temp = Fk(key1, right_half)
    right_half = [left_half[i] ^ temp[i] for i in range(len(temp))]

    left_half, right_half = right_half, left_half

    temp = Fk(key2, right_half)
    right_half = [left_half[i] ^ temp[i] for i in range(len(temp))]

    cipher_text = permute(left_half + right_half, FP)
    return cipher_text

def decrypt(cipher_text, key):
    key1, key2 = generate_keys(key)
    cipher_text = permute(cipher_text, IP)

    left_half = cipher_text[:4]
    right_half = cipher_text[4:]

    temp = Fk(key2, right_half)
    right_half = [left_half[i] ^ temp[i] for i in range(len(temp))]

    left_half, right_half = right_half, left_half

    temp = Fk(key1, right_half)
    right_half = [left_half[i] ^ temp[i] for i in range(len(temp))]

    plain_text = permute(left_half + right_half, FP)
    return plain_text

# Example Usage
plain_text = '10101010'
key = '1010000010'

cipher_text = encrypt(plain_text, key)
decrypted_text = decrypt(cipher_text, key)

print("Plaintext:", plain_text)
print("Key:", key)
print("Ciphertext:", cipher_text)
print("Decrypted Text:", decrypted_text)
