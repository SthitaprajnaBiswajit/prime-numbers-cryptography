# Sieve of Eratosthenes to find prime numbers up to n
def find_primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False

    return [i for i, prime in enumerate(is_prime) if prime]

# Example usage
n = int(input("Enter upper limit to find primes: "))
primes = find_primes(n)
print(f"Prime numbers up to {n} are:")
print(primes)
