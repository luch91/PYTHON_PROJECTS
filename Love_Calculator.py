"""
Take both people's names and check for the number of times the word TRUE occurs, then 
check for the number of times the word LOVE occurs. Combine the numbers to make a 
2 digit number. 
For love scores less than 10 or greater than 90, the message should be:
"Your love score is x, you go together like coke and menthos"
For scores between 40 and 55, the message should be:
"Your love  score is x, you are alright together"
For love score between 55 and 90, the message should be:
Your love  score is x, you are a match made in heaven


Otherwise, the message should be:
"Your score is x, you are a disaster-in-waiting
"""
print("Welcome to Love Calculator!!, Let's Find out if you and your crush are meant to be")
name = input("What is your name? ")
crush = input("what is the name of your spouse? ")
name = name.lower()
crush = crush.lower()

combined_name = name + crush

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

true = t + r + u + e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l + o + v + e

love_cal = int(str(true )+ str(love ))
l
print(love_cal)

if love_cal < 10 or love_cal > 90:
    print(f"Your love score is {love_cal}, you go together like coke and menthos")
elif love_cal >= 40 and love_cal <= 54:
    print(f"Your love score is {love_cal}, you are alright together")
elif love_cal >= 55 and love_cal <= 90:
    print(f"Your love score is {love_cal}, you are a match made in heaven")
else:
    print(f"Your love score is {love_cal}, you are a disaster-in-waiting")
