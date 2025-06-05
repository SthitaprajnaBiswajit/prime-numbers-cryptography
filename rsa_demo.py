# RSA Encryption and Decryption in Python
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = gcd_extended(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    g, x, _ = gcd_extended(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

# Step 1: Choose two primes
p = 11
q = 13
n = p * q
phi = (p - 1) * (q - 1)

# Step 2: Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = 7

# Step 3: Find modular inverse of e
d = mod_inverse(e, phi)

print(f"Public Key: ({e}, {n})")
print(f"Private Key: ({d}, {n})")

# Step 4: Message encryption and decryption
message = 9
cipher = pow(message, e, n)
decrypted = pow(cipher, d, n)

print(f"Original Message: {message}")
print(f"Encrypted Message: {cipher}")
print(f"Decrypted Message: {decrypted}")
