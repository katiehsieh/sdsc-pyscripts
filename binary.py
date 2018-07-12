import random

decimalValue = int(input("Enter an integer >= 0: "))
number = decimalValue
binaryResult = []

while number > 0:
    # Find mod 2
    binaryResult.append(number % 2)
    # Find number // 2
    number = number // 2

print(decimalValue, "in binary is", end=" ")

# Print method 1
for i in range(len(binaryResult)-1, -1, -1):
    print(binaryResult[i], end="")

print()

# Print method 2
first = 0
second = len(binaryResult) - 1

while first < second:
    temp = binaryResult[first]
    binaryResult[first] = binaryResult[second]
    binaryResult[second] = temp
    first += 1
    second -= 1

for element in binaryResult:
    print(element, end="")
