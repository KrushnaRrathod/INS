import math

def columnar_transposition_encrypt(plaintext, keyword):
    keyword_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    num_columns = len(keyword)
    num_rows = math.ceil(len(plaintext) / num_columns)
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    for i, char in enumerate(plaintext):
        matrix[i // num_columns][keyword_order[i % num_columns]] = char

    ciphertext = ''.join(''.join(row) for row in matrix)
    return ciphertext

def columnar_transposition_decrypt(ciphertext, keyword):
    keyword_order = sorted(range(len(keyword)), key=lambda k: keyword[k])
    num_columns = len(keyword)
    num_rows = math.ceil(len(ciphertext) / num_columns)
    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]

    index = 0
    for i in range(num_columns):
        for j in range(num_rows):
            matrix[j][keyword_order[i]] = ciphertext[index]
            index += 1
            if index == len(ciphertext):
                break

    plaintext = ''.join(''.join(row) for row in matrix)
    return plaintext

# Example Usage
plaintext = "HELLO WORLD"
keyword = "KEY"
encrypted_text = columnar_transposition_encrypt(plaintext, keyword)
decrypted_text = columnar_transposition_decrypt(encrypted_text, keyword)

print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
