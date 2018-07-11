print("Welcome to fibonacci")

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter an integer > 2: "))

while n > 0:
    print("Term " + str(n) + " in the fibonacci sequence is: " + str(fibonacci(n)))
    n -= 1
