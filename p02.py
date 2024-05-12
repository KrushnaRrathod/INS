import random

def generate_random_key():
    # Generate a random permutation of the alphabet
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    random.shuffle(alphabet)
    return ''.join(alphabet)

def monoalphabetic_cipher_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += key[ord(char) - 97]
            elif char.isupper():
                encrypted_text += key[ord(char) - 65].upper()
        else:
            encrypted_text += char
    return encrypted_text

def monoalphabetic_cipher_decrypt(text, key):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr(key.index(char.lower()) + 97)
            elif char.isupper():
                decrypted_text += chr(key.index(char.lower()) + 97).upper()
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
plaintext = "Hello, World!"
key = generate_random_key()
print("Random key:", key)

encrypted_text = monoalphabetic_cipher_encrypt(plaintext, key)
print("Encrypted text:", encrypted_text)

decrypted_text = monoalphabetic_cipher_decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
