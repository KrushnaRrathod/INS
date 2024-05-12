import re

def prepare_text(text):
    # Remove non-alphabetic characters and convert to uppercase
    text = re.sub(r'[^a-zA-Z]', '', text).upper()
    # Replace 'J' with 'I'
    text = text.replace('J', 'I')
    return text

def generate_key_matrix(key):
    # Initialize key matrix with 5x5 dimension
    key_matrix = [['' for _ in range(5)] for _ in range(5)]
    # Fill key matrix with unique characters from the key
    key = prepare_text(key)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' # Exclude 'J'
    key_index = 0
    for i in range(5):
        for j in range(5):
            if key_index < len(key):
                key_matrix[i][j] = key[key_index]
                key_index += 1
            else:
                # Fill remaining matrix cells with remaining alphabet characters
                for char in alphabet:
                    if char not in ''.join(key_matrix[i]):
                        key_matrix[i][j] = char
                        break
    return key_matrix

def find_char(char, key_matrix):
    # Find the position of a character in the key matrix
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == char:
                return i, j

def playfair_cipher_encrypt(text, key):
    key_matrix = generate_key_matrix(key)
    text = prepare_text(text)
    encrypted_text = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else 'X'
        row1, col1 = find_char(char1, key_matrix)
        row2, col2 = find_char(char2, key_matrix)
        if row1 == row2: # Same row
            encrypted_text += key_matrix[row1][(col1 + 1) % 5]
            encrypted_text += key_matrix[row2][(col2 + 1) % 5]
        elif col1 == col2: # Same column
            encrypted_text += key_matrix[(row1 + 1) % 5][col1]
            encrypted_text += key_matrix[(row2 + 1) % 5][col2]
        else: # Different rows and columns
            encrypted_text += key_matrix[row1][col2]
            encrypted_text += key_matrix[row2][col1]
    return encrypted_text

def playfair_cipher_decrypt(text, key):
    key_matrix = generate_key_matrix(key)
    text = prepare_text(text)
    decrypted_text = ""
    for i in range(0, len(text), 2):
        char1 = text[i]
        char2 = text[i + 1] if i + 1 < len(text) else 'X'
        row1, col1 = find_char(char1, key_matrix)
        row2, col2 = find_char(char2, key_matrix)
        if row1 == row2: # Same row
            decrypted_text += key_matrix[row1][(col1 - 1) % 5]
            decrypted_text += key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2: # Same column
            decrypted_text += key_matrix[(row1 - 1) % 5][col1]
            decrypted_text += key_matrix[(row2 - 1) % 5][col2]
        else: # Different rows and columns
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]
    return decrypted_text

# Example usage:
plaintext = "Hide the gold in the tree stump"
key = "playfair example"
encrypted_text = playfair_cipher_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = playfair_cipher_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
