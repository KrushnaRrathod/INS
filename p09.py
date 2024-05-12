import random

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Function to generate a random prime number of a given length
def generate_prime_number(length):
    while True:
        num = random.randrange(2**(length-1), 2**length)
        if is_prime(num):
            return num

# Function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to generate public and private keys
def generate_keys(bit_length):
    p = generate_prime_number(bit_length)
    q = generate_prime_number(bit_length)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randrange(2, phi)
        if gcd(e, phi) == 1:
            break

    d = pow(e, -1, phi)

    return (e, n), (d, n)

# Function to encrypt a message using RSA
def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

# Function to decrypt a message using RSA
def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Example Usage
bit_length = 8  # bit length for prime numbers (adjust for security level)
public_key, private_key = generate_keys(bit_length)

message = "Hello, RSA!"
print("Original Message:", message)

encrypted_message = encrypt(message, public_key)
print("Encrypted Message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted Message:", decrypted_message)
