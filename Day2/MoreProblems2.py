# 2. Write a program to find simple interest on a principal amount A at interest rate of R for time period T. Take A, R and T as input from the user.
A = float(input('Enter principal amount: '))
R = float(input('Enter interest rate: '))
T = float(input('Enter time period: '))

print("Simple Interest is",(A*R*T)/100)
