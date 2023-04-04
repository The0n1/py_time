#!/usr/bin/env python3

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tipping calculator!\n")

# Gathering input from user
total_bill = float(input("How much was the bill? $"))
total_tip_percent = int(
    input("How much would you like to tip (10, 12, 15, etc)? "))
sales_tax_percent = float(input("What is the sales tax (8.00, 8.25, 9.00, etc)? "))
total_guest = int(input("How many people are you splitting the bill with? "))

# Calculating how much tip
total_tip = float(total_bill * total_tip_percent / 100)

# Calculating tax
total_sales_tax = float(total_bill * sales_tax_percent / 100)

# Calculating how much each guest owes
final_payment = round((total_bill + total_tip + total_sales_tax) / total_guest,
                      2)

print(f"\nEach person should pay... ${final_payment:.2f}")