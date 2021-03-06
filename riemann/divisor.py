'''Compute the sum of divisors of a number.'''
from functools import lru_cache
from riemann.types import RiemannDivisorSum
from typing import List, Tuple
from numba import njit
import math


@njit
def divisor_sum(n: int) -> int:
    '''Compute the sum of divisors of a positive integer.'''
    if n <= 0:
        return 0
    
    i = 1
    limit = math.sqrt(n)
    the_sum = 0
    while i <= limit:
        if n % i == 0:
            the_sum += i
            if i != limit:
                the_sum += n // i
        i += 1
    return the_sum


@njit
def prime_factor_divisor_sum(prime_factors: List[Tuple[int]]) -> int:
    '''Compute the sum of the divisors of a positive integer
    expressed in its prime factorization
    '''
    if not prime_factors:
        return 1
    
    divisor_sum = 1
    for (prime, exponent) in prime_factors:
        divisor_sum *= int((prime ** (exponent + 1) - 1) / (prime - 1))
    
    return divisor_sum


@njit
def witness_value(n: int, precomputed_divisor_sum=None) -> float:
    denominator = n * math.log(math.log(n))
    ds = precomputed_divisor_sum or divisor_sum(n)
    return ds / denominator


def compute_riemann_divisor_sums(start_n: int, end_n: int) -> List[RiemannDivisorSum]:
    '''Compute a batch of divisor sums.'''
    output = [None] * (end_n - start_n + 1)
    for n in range(start_n, end_n + 1):
        ds = divisor_sum(n)
        wv = witness_value(n, precomputed_divisor_sum=ds)
        output[n - start_n] = RiemannDivisorSum(n=n, divisor_sum=ds, witness_value=wv)
    
    return output
