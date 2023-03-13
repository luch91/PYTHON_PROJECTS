'''
Ask for two numbers.If the first one is larger than the second, 
display the second one first and then the first one, otherwise
show the first one number first and the second

num1 = int(input('Enter the first number: '))
num2 = int(input("Enter the second: "))
result = num1 +num2
if num1 > num2:
    print(num2, num1)
else:
    print(num2, num1)
'''
    
    
'''
Ask the user to enter a number between 10 and 20
(inclusive). If they enter a number within this range,
display the message “Thank you”, otherwise display the
message “Incorrect answer"
'''

'''num = int(input('Enter a number between 10 and 20: '))
if num >=10 and num <=20:
    print("Thank you")
else:
    print("Incorrect number")'''

'''
Ask the user to enter their favourite colour. If they enter “red”, “RED” or
“Red” display the message “I like red too”, otherwise display the message
“I don’t like [colour], I prefer red”.

'''

'''
colour = input("Enter your favourite colour: ")
if colour == 'RED' or colour == 'red' or colour == 'Red':
    print("I love red also")
else:
    print("I don't like", colour, "I prefer red")

'''

'''
 **Eligible to vote or not**:
Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the
message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are
under 16, display the message “You can go Trick- or-Treating”.
'''

'''age = int(input('what is your age? '))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can go buy a lottery ticket")
else:
    print('You can go Trick- or-Treating')'''


'''
Be a Nosy Neighbour

Ask the user if it is raining and convert their answer to lower case
so it doesn’t matter what case they type it in. If they answer “yes”,
ask if it is windy. If they answer “yes” to this second question,
display the answer “It is too windy for an umbrella”, otherwise
display the message “Take an umbrella”. If they did not answer yes
to the first question, display the answer “Enjoy your day”
'''

'''raining = str.lower(input('Is it raining? '))
if raining == 'yes':
    windy = str.lower(input('Is it windy? '))
    if windy == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')

else:
    print('Enjoy your day')
'''


#Check Your BMI, how healthy are you?
"""Weight in Kg / Height in m2
Weight / H x h
If BMI
	< 16 . = You are severely underweight
	16 - 17, You're moderately underweight
	17.1 - 18.4, You're midly underweight
	18.5 - 25, Your weight is normal
	25.1 - 29, You're slightly overweight
	30 - 40,  You're moderatly obese
	> 40, You have morbid obesity. Visit a Dietitian
"""
"""
print('Check Your BMI, how healthy are you?')
weight = float(input("What is your weight in kg? "))
height = float(input('What is your height in m? '))
height = height * height

BMI = float(weight/height)
BMI = round(BMI, 2) #rounds the float to two decimal places
print(BMI, "Kg/m2")

if BMI < 16.0:
    print("You are severely underweight")
elif BMI >= 16 and BMI <= 17.0:
    print("You are moderately underweight")
elif BMI >= 17.1 and BMI <= 18.4 :
    print("You are midly underweight")
elif BMI >= 18.5 and BMI <= 25.0 :
    print("You weight is normal")
elif BMI >= 25.1 and BMI <= 29:
    print("You are slightly overweight")
elif BMI >=30 and BMI <=40:
    print("You're moderatly obese")
else:
    print("You have morbid obesity. Visit a Dietitian")
    

"""
"""Pig Latin takes the first consonant of a word,
moves it to the end of the word and adds on an
“ay”. If a word begins with a vowel you just add
“way” to the end. For example, pig becomes igpay,
banana becomes ananabay, and aadvark becomes
aadvarkway. Create a program that will ask the
user to enter a word and change it into Pig Latin.
Make sure the new word is displayed in lower case.
"""

"""word = input("Enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if first != "a" and first != "e" and first != "i" and first !="o" and first !="u" :
    pig_latin = rest + word[0] + "ay"
else:
    pig_latin = word + "way"
print(pig_latin)
"""

"""
Display the following message:
1. Square
2. Triangle
Enter a number:

If the user enters 1, then it should ask them for
the length of one of its sides and display the
area. If they select 2, it should ask for the base
and height of the triangle and display the area. If
they type in anything else, it should give them a
suitable error message.
"""

print("1. Square")
print("2. Triangle")
selection = int(input("Enter a number: "))
if selection == 1:
    length = input("what is the length of one side of the Triangle? ")
    area = length * length
    print(f"The area of the selected option is {area} ")

elif selection  == 2:
    base = int(input("what is the base of the triangle? "))
    height = int(input("what is the height of the triangle? "))
    area = (base * height)/ 2
    print(f"The area of the selected option is {area} ")

else:
    print("Wrong selection, please select between 1 and 2")
