# The FizzBuzz Program: Print numbers from 1-100, if number is divisible by 3, print fizz, 
# if the number is divisible by 5, print buzz, if the number is divisible by both 3 and 5 then print fizzbuzz
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
