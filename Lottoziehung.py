import random

zahlen = list(range(0, 46))  # 0 bis 45
gezogeneZahlen = [0] * 45

def ablauf(counter):
    while counter < 7:
        zufallszahl = random.randint(1, 45 - counter)
        zahlen[45 - counter], zahlen[zufallszahl] = zahlen[zufallszahl], zahlen[45 - counter]
        counter += 1

    print(zahlen[45 - counter + 1:45])

    for i in range(6):
        gezogeneZahlen[zahlen[45-i]-1] = gezogeneZahlen[zahlen[45-i]-1] + 1

for i in range(1000):
    counter = 0
    ablauf(counter)

print(gezogeneZahlen)