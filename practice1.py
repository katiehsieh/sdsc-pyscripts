import pygame

firstName = input("What's your first name? ")
lastName = input("What's your last name? ")
age = int(input("How old are you, " + firstName + "? "))

print("Hello, " + firstName + " " + lastName)

if age >= 30:
    print("You're very young!")
else:
    print("Not so young!")
