def rail_fence_encrypt(plaintext, rails):
    fence = [[] for _ in range(rails)]
    rail = 0
    direction = 1

    for char in plaintext:
        fence[rail].append(char)
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction

    ciphertext = ''.join([''.join(rail) for rail in fence])
    return ciphertext

def rail_fence_decrypt(ciphertext, rails):
    fence = [['' for _ in ciphertext] for _ in range(rails)]
    rail = 0
    direction = 1

    for i, char in enumerate(ciphertext):
        fence[rail][i] = char
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction

    plaintext = ''
    rail = 0
    direction = 1

    for _ in range(len(ciphertext)):
        plaintext += fence[rail][_]
        rail += direction
        if rail == rails - 1 or rail == 0:
            direction = -direction

    return plaintext

# Example Usage
plaintext = "HELLO WORLD"
rails = 3
encrypted_text = rail_fence_encrypt(plaintext, rails)
decrypted_text = rail_fence_decrypt(encrypted_text, rails)

print("Plaintext:", plaintext)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
