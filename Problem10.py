# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from utils import generatePrimes

def main():
    print(sum(generatePrimes(2000000)))

if(__name__ == "__main__"):
    main();
