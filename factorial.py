print("Welcome to Recursion")

# non recursive factorial function
def nonRfactorial(n):
    nonRecursiveAnswer = 1
    while n >= 1:
        nonRecursiveAnswer *= n
        n -= 1
    return nonRecursiveAnswer

# recursive factorial function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter an integer >= 0: "))

print("Non Recursive: " + str(n) + "! = " + str(nonRfactorial(n)))
print("Recursive: " + str(n) + "! = " + str(factorial(n)))
