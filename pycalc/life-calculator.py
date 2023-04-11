#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
age = int(input("What is your current age? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Total life
total_days = 90 * 365
total_weeks = 90 * 52
total_months = 90 * 12

# Lived
lived_days = age * 365
lived_weeks = age * 52
lived_months = age * 12

# Time left
left_days = int(total_days - lived_days)
left_weeks = int(total_weeks - lived_weeks)
left_months = int(total_months - lived_months)

# Print
print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")
