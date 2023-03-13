"""
Your program should print each number from 1 to 100
When the number is divisible by 3 then instead of printing the number,
it should print 'Fizz'
And if the number is divisible by 5, then instead of printing the number,
it should print 'Buzz'
And if the number is divisible by both 3 and 5 ,
it should print 'Fizzbuzz instead of the number
"""
for number in range(1, 101):
    if number % 3 ==0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
