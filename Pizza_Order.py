"""
Create a pizza order program. Ask the user what size of pizza they want, S, M and L.
Ask whether they want to add pepperoni to it.
Also ask if they want to add extra cheese.
Small pizza : $15
medium pizza : $20
Large : $25
Pepperoi for small pizza : $2
Pepperoni for medium or large = $3

Extra cheese for any size pizza = $1

"""
print("Welcome to pizza hut")

pizza_size = input("What size of pizza do you want, S, M, or L? ")
pepperoni = input("Do you want to add pepperoni? Y or N ")
cheese = input("Do you want to add cheese? Y or N ")

bill = 0
if pizza_size == "S":
    bill = 15
    if pepperoni =="Y":
        bill += 2
    if cheese == "Y" :
        bill += 1
    print(f"Your total bill is ${bill} ")
elif pizza_size == "M" :
    bill = 20
    if pepperoni == "Y" :
        bill += 3
    if cheese == "Y":
        bill +=1
    print(f"Your total bill is ${bill} ")
else:
    bill = 25
    if pepperoni == "Y":
       bill +=3
    if cheese == "Y" :
       bill += 1
    print(f"Your total bill is ${bill} ") 
    
print("Thank you for shopping with us")

#cleaner code

if pizza_size == "S" :
    bill += 15
elif pizza_size == "M":
    bill += 20
else :
    bill += 25

if pepperoni == "Y":
    if pizza_size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1
print(f"Your total bill is ${bill} ") 
print("Thank you for shopping with us")
