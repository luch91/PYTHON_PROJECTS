"""
Define a subprogram that will ask the user to
enter a number and save it as the variable
“num”. Define another subprogram that will
use “num” and count from 1 to that number.
"""

"""def  ask_value():
    num = int(input("input a number: "))
    return num

def count(num):
    n = 1
    while n <= num:
        print(n)
        n = n + 1

def main():
    num = ask_value()
    count(num)


main()"""


"""
Display the following menu to the user:
1)Addition
2)Subtraction

Enter 1 or 2
If they enter a 1, it should run a subprogram that will
generate two random numbers between 5 and 20, and
ask the user to add them together. Work out the correct
answer and return both the user’s answer and the
correct answer.

If they entered 2 as their selection on the menu, it
should run a subprogram that will generate one number
between 25 and 50 and another number between 1 and
25 and ask them to work out num1 minus num2.

This way they will not have to worry about negative answers.
Return both the user’s answer and the correct answer.
Create another subprogram that will check if the user’s
answer matches the actual answer. 

If it does, display “Correct”, otherwise display a message
 that will say “Incorrect, the answer is” and display the real answer.
If they do not select a relevant option on the first menu
you should display a suitable message.
"""

import random

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    user_answer = int(input("Your answer: "))
    correct_answer = num1 + num2
    print(f"num1 + num2 = {num1} + {num2} ")
    answers = (user_answer, correct_answer)
    return answers

def subtraction():
    num3 = random.randint(25, 50)
    num4 = random.randint(1,25)
    print(f"num3 - num4 = {num3} + {num4}")
    user_answer = int(input("Guess the answer: "))
    correct_answer = num3 - num4
    answers = (user_answer, correct_answer)
    return answers

def checker(user_answer, correct_answer):
    "checks and compares the user and the correct answer"
    if user_answer == correct_answer:
        print(f"Correct, the score is {correct_answer}")
    else:
        print(f"Incorrect, the real score {correct_answer}")



def menu():
    print("1) Addition")
    print("2) Subtraction")
    user_choice = int(input("Enter 1 or 2 : "))
    if user_choice == 1:
        user_answer, correct_answer = addition()
        checker(user_answer, correct_answer)   
    elif user_choice == 2:
        user_answer, correct_answer = subtraction()
        checker(user_answer, correct_answer)
    
    else:
        print("Incorrect selection")

menu()



    
 

"""
Create a program that will allow the user to easily manage a list of names. You should
display a menu that will allow them to add a name to the list, change a name in the
list, delete a name from the list or view all the names in the list. There should also be a
menu option to allow the user to end the program. If they select an option that is not
relevant, then it should display a suitable message. After they have made a selection
to either add a name, change a name, delete a name or view all the names, they
should see the menu again without having to restart the program. The program
should be made as easy to use as possible.
"""
names = []
def add_name():
    name = input( "Entae a new name")
    names.append(name)
    return names

def change_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
        select_num = int(input("Enter the number of the name you want to change: "))
        name = input("Enter a new name: ")
        names[select_num] = name
        return names
    
def delete_name():
    num = 0
    for x in names:
        print(num, x)
        num = num + 1
    select_num = int(input("Enter the number of the name you want to delete: "))
    del names[select_num]
    return names

def view_names():
    for x in names:
        print(x)
    print()


def main():
    again = "y"
    while again == "y":
        print("1. Add a name")
        print("2) Change a name")
        print("3) Delete a name")
        print("4) View a name")
        print("5)Quit")
        selection = int(input("What do you want to do?"))
        if selection == 1:
            names = add_name()
        elif selection == 2:
            names = change_name()
        elif selection == 3:
            names = delete_name()
        elif selection == 4:
            names = view_names()
        elif selection == 5:
            again = "n"
        else:
            print("Incorrect option: ")
        data = (names, again)

main()





        

