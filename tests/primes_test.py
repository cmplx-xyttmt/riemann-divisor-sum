import pytest
from riemann.primes import generate_primes_up_to_n


# number of primes less than 10, 100, 1000, 10000, 100000, 1000000
pow_10_num_of_primes = [4, 25, 168, 1229, 9592, 78498]

num_prime_pair = zip([10**i for i in range(1, 7)], pow_10_num_of_primes)


def test_generate_primes_up_to_20():
    expected = [2, 3, 5, 7, 11, 13, 17, 19]
    assert generate_primes_up_to_n(20) == expected


@pytest.mark.parametrize("n,num_of_primes", num_prime_pair)
def test_number_of_primes(n, num_of_primes):
    assert len(generate_primes_up_to_n(n)) == num_of_primes
