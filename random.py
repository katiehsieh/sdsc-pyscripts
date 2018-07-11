import random

highValue = 6000000
ones = 0
twos = 0
threes = 0
fours = 0
fives = 0
sixes = 0

while highValue > 0:
    #print(random.randint(1,6), end=" ")
    temp = random.randint(1,6)
    if temp == 1:
        ones += 1
    elif temp == 2:
        twos += 1
    elif temp == 3:
        threes += 1
    elif temp == 4:
        fours += 1
    elif temp == 5:
        fives += 1
    else:
        sixes += 1
        
    highValue = highValue - 1

print("Ones: " + str(ones))
print("Twos: " + str(twos))
print("Threes: " + str(threes))
print("Fours: " + str(fours))
print("Fives: " + str(fives))
print("Sixes: " + str(sixes))
