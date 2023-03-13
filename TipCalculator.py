"""
A tip calculator. The calculator asks what the total bill is.
It then asks wjat percentage tip you would like to tip and how
many people are to split the bill.
Then it gives an output of the amunt each person should pay
There are two ways this calculation can work:

percentage = Divide the percentage tip by 100.
total_tip = Multiply the total bill by percentage
total_bill = bill + total_tip
bill_per_person = Divide the total bill by the number of persons.


Solution 2:
(bill/ number of persons) * (1 + percentage)
E.g, if the bill was 120usd, each person should pay
(120.00/ 5) *( 1 + 0.12)
(120.00/ 5) * 1.10

"""
#solution1:

print("Welcome to tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
total_tip = float(bill * tip/100 )
total_bill = bill + total_tip
bill_per_person = total_bill/ people
final_bill = "{:.2f}".format(bill_per_person)  #rounds to 2 decimal places.
print("Each person should pay", final_bill)

#solution2:

print("Welcome to tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percentage = tip/100
tip_as_percentage += 1
bill_per_person = bill/people
final_bill = bill_per_person * (tip_as_percentage )
final_bill = "{:.2f}".format(final_bill)  #rounds to 2 decimal places
print("Each person should pay", final_bill)


