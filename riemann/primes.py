from typing import List


def generate_primes_up_to_n(n: int) -> List[int]:
    '''Uses the sieve of eratosthenes to generate primes <= n'''
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for x in range(2, n + 1):
        if not is_prime[x]:
            continue
        for u in range(2 * x, n + 1, x):
            is_prime[u] = False
    
    return [i for i in range(1, n + 1) if is_prime[i]]
