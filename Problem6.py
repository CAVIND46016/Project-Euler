# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)^2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumOfSquare(_count):
    return ((_count) * (_count + 1) * (2 * _count + 1)) / 6;

def squareOfSum(_count):
    sum = ((_count) * (_count + 1)) / 2;
    return sum * sum;

def main():
    count = 100;
    print("{}".format(int(squareOfSum(count) - sumOfSquare(count))));

if __name__ == "__main__":
    main();
