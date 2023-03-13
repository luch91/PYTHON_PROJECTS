for i in range(20, 2, -3): #this prints in descending order by subtracting 3.
    print(i)

"""
Ask the user to enter their name and then
display their name three times.
"""


name = input("Enter your name: ")
for i in range(0,3):
    print(name)
   

"""
Alter program 035 so that it will ask the user to enter their
name and a number and then display their name that
number of times.
"""

name = input("Enter a name: ")
number = int(input("Enter a number: "))
for i in range (0, number):
    print(name)
    

"""Change program to also ask for a
number. Display their name (one
letter at a time on
each line) and repeat this for the
number of times they entered.
"""


number = int(input("Enter a number"))
name = input("Enter your name")
for x in range(0, number):
    for i in name:
        print(i)


"""
Ask the user to enter a number between 1
and 12 and then display the times table for
that number.
"""

number = int(input("Enter a number between 1 and 12: "))
for i in range(0, 13):
    answer = i * number
    #print(i, "X",number, "=", answer)
    print(f"{i} x {number} = {answer}")


"""
Ask for a number below 50 and then count down from
50 to that number, making sure you show the number
they entered in the output.
"""

number = int(input("Enter a number below 50: "))
for i in range(50, number-1, -2):
    print(i)


"""
Ask the user to enter their name and a number. If the
number is less than 10, then display their name that
number of times; otherwise display the message “Too
high” three times
"""

name = input("Enter your name: ")
num1 = int(input("Enter a number: "))
if num1 <= 10:
    for i in range(0, num1):
        print(name)
else:
    for i in range(0, 3):
        print("Too high")



"""
Set a variable called total to 0. Ask the user to enter
five numbers and after each input ask them if they
want that number included. If they do, then add the
number to the total. If they do not want it included,
don’t add it to the total. After they have entered all five
numbers, display the total.
"""
total = 0
for i in range(0, 5):
    num = int(input("Enter a number: "))
    ans = input("Do you want this number to be included? (y/n)")
    if ans == "y":
        total = total + num
print(total)

"""
Ask which direction the user wants to count (up or down). If they select up, then ask
them for the top number and then count from 1 to that number. If they select down, ask
them to enter a number below 20 and then count down from 20 to that number. If they
entered something other than up or down, display the message “I don’t understand”
"""

direction = input("Do you want to count up or down? (u/d) ")
if direction == "u":
    num = int(input("What is the top number? "))
    for i in range(1, num+1):
        print(i)
elif direction == "d":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num-1, -1):
        print(i)
else:
    print("I don't remember")

"""
A program to calculate the highest score 
"""
highest_score = 0
scores = [3, 18, 89, 102, 190, 34, 278, 67, 278, 239]
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"highest score is: {highest_score}")

"""
print the total number from 1 to 100.
"""
total = 0
for number in range(1, 101):
    total += number
print(total)

"""
Add up all the even number between 1 and 100
"""

#solution 1:
total = 0
for number in range(2, 100, 2):
    total +=number
print(total)

#solution 2

total = 0
for number in range(1, 100):
    if number % 2 == 0:
        total += number
print(total)


  

