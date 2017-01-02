# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# http://mathforum.org/library/drmath/view/65801.html

def largestPrimeFactor(_inputNumber):
    var = 2;
    while var * var <= _inputNumber:
        if (_inputNumber % var):
            var = var + 1;
        else:
            _inputNumber //= var;
            
    return _inputNumber;

def main():
    inputNumber = 600851475143;
    print("Largest prime factor of {}: {}".format(inputNumber, largestPrimeFactor(inputNumber)));

if __name__ == "__main__":
    main();