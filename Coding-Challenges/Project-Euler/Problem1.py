# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def getSum(_initial, _final):
    sum = 0;
    for counter in range(_initial, _final):
        if(counter % 3 == 0 or counter % 5 == 0):
            sum = sum + counter;
    return sum;

def main():
    print("Sum of all multiples of 3 or 5 below 1000: {}".format(getSum(1, 1000)));
    
if __name__ == "__main__":
    main();
        
