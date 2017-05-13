#Vinicius Sesti <vinicius.s.sesti@gmail.com>
#
#Project Euler: Problem 6
#
#The sum of the squares of the first ten natural numbers is,
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#summing the squares of the first n numbers gets us n(n+1)(2n+1)/6, so lets just use that
def sumSquares(n):
    return n*(n+1)*(2*n+1)/6

#likewise, summing the first n numbers is n(n+1)/2
def squareSum(n):
    return (n*(n+1)/2)**2

if __name__ == '__main__':
    n = int(input())
    diff = squareSum(n)-sumSquares(n) 
    print(str(diff))
