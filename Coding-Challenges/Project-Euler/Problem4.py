#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def check_Palindrome(_num):
    return str(_num) == str(_num)[::-1];

def main():
    product = 0;
    listPalin = [];
    
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j;
            if(check_Palindrome(product)):
                listPalin.append(product);
    
    print(str(max(listPalin)));

if(__name__ == "__main__"):
    main();