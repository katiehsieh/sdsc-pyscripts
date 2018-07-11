import random

highToss = 200
heads = 0
tails = 0

while highToss > 0:
    coin = random.randint(1,2)
    if coin == 1:
        heads += 1
    else:
        tails += 1

    highToss = highToss - 1

print("Heads: " + str(heads))
print("Tails: " + str(tails))
