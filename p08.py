# Function to calculate (base^exp) % mod
def power(base, exp, mod):
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp = exp // 2
        base = (base * base) % mod
    return res

# Function to generate the public key
def generate_public_key(base, private_key, prime):
    return power(base, private_key, prime)

# Function to generate the shared secret key
def generate_shared_secret(public_key, private_key, prime):
    return power(public_key, private_key, prime)

# Example Usage
# Common prime number shared by both parties
prime = 23
# Common base shared by both parties
base = 5

# Private keys of both parties
private_key_a = 6
private_key_b = 15

# Alice calculates her public key and sends it to Bob
public_key_a = generate_public_key(base, private_key_a, prime)

# Bob calculates his public key and sends it to Alice
public_key_b = generate_public_key(base, private_key_b, prime)

# Alice calculates the shared secret key
shared_secret_a = generate_shared_secret(public_key_b, private_key_a, prime)

# Bob calculates the shared secret key
shared_secret_b = generate_shared_secret(public_key_a, private_key_b, prime)

print("Alice's Public Key:", public_key_a)
print("Bob's Public Key:", public_key_b)
print("Shared Secret Key (Calculated by Alice):", shared_secret_a)
print("Shared Secret Key (Calculated by Bob):", shared_secret_b)
