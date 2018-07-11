import pygame

for number in range(1,101):
    print(number, ":", end=" ")
    for divisor in range(1,number+1):
        if number % divisor == 0:
            print(divisor, end=" ")
    print()
