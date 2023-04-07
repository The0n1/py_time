#!/usr/bin/env python3

import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

# Generate a random winner
winner = random.choice(names)

print(winner + " is going to buy the meal today!")