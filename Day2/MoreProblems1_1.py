# 1. Write a program to find sum all Natural numbers from 1 to N where you have to take N as input from user
n = int(input('Enter a natural number: '))
def sum_natural(n):
    sum = 0
    while n > 0:
        sum = sum + n
        n = n-1
    print(sum)
    
sum_natural(n)
