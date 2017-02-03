# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers
# File: D\Problem13.txt

def firstTenDigits(_number):
    return str(_number)[:10];    
        
def main():
    inputFile = open("D:\\Problem13.txt", 'r');
    sum = 0;
    for num in inputFile:
        sum = sum + int(num); 
        
    print("First ten digits: {}".format(firstTenDigits(sum)));    
    
if __name__ == "__main__":
    main();
