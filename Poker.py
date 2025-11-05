import random
from tabulate import tabulate

def main():
    karten = list(range(52))  # 0-51
    counterH = 0
    counterP = 0
    counterZP = 0
    counterD = 0
    counterS = 0
    counterF = 0
    counterFH = 0
    counterV = 0
    counterSF = 0
    counterRF = 0
    for i in range(100000):
        gezogene_karten = ziehung()
        kombi = kombinationen(gezogene_karten)
        if kombi == 0:
            counterH = counterH + 1
        elif kombi == 1:
            counterP = counterP + 1
        elif kombi == 2:
            counterZP = counterZP + 1
        elif kombi == 3:
            counterD = counterD + 1
        elif kombi == 4:
            counterS = counterS + 1
        elif kombi == 5:
            counterF = counterF + 1
        elif kombi == 6:
            counterFH = counterFH + 1
        elif kombi == 7:
            counterV = counterV + 1
        elif kombi == 8:
            counterSF = counterSF + 1
        elif kombi == 9:
            counterRF = counterRF + 1


    print(f" Hohe Karte: {(counterH / 100000) * 100:.3f}% ({counterH}),\n "
          f"Paar: {(counterP / 100000) * 100:.3f}% ({counterP}),\n "
          f"Zwei Paare: {(counterZP / 100000) * 100:.3f}% ({counterZP}),\n "
          f"Drilling: {(counterD / 100000) * 100:.3f}% ({counterD}),\n "
          f"Straße: {(counterS / 100000) * 100:.3f}% ({counterS}),\n "
          f"Flush: {(counterF / 100000) * 100:.3f}% ({counterF}),\n "
          f"Full House: {(counterFH / 100000) * 100:.3f}% ({counterFH}),\n "
          f"Vierling: {(counterV / 100000) * 100:.3f}% ({counterV}),\n "
          f"Straight Flush: {(counterSF / 100000) * 100:.3f}% ({counterSF}),\n "
          f"Royal Flush: {(counterRF / 100000) * 100:.5f}% ({counterRF})")

def ziehung():
    karten = list(range(52))
    for i in range(5):
        zufallszahl = random.randint(0, 51 - i)
        karten[51 - i], karten[zufallszahl] = karten[zufallszahl], karten[51 - i]

    return karten[-5:]  #letzte 5 Karten

def kombinationen(ziehung):
    farbe = []
    figur = []
    for i in ziehung:
        farbe.append(i // 13)  #0–3
        figur.append(i % 13)   #0–12

    farbe.sort()
    figur.sort()

    for i in range(len(farbe) - 4):  # 0
        if farbe[i] == farbe[i + 1] == farbe[i + 2] == farbe[i + 3] == farbe[i + 4] and figur[i] == 0 and figur[i + 1] == 9 and figur[i + 2] == 10 and figur[i + 3] == 11 and figur[i + 4] == 12:
            ergebnis = 9  #Royal Flush
            # print("Royal Flush")
            return ergebnis

    for i in range(len(farbe) - 4):  # 0
        if farbe[i] == farbe[i + 1] == farbe[i + 2] == farbe[i + 3] == farbe[i + 4] and figur[i] == figur[i + 1] - 1 == figur[i + 2] - 2 == figur[i + 3] - 3 == figur[i + 4] - 4:
            ergebnis = 8  #Straight Flush
            # print("Straight Flush")
            return ergebnis

    for i in range(len(figur) - 3):  # 0,1
        if figur[i] == figur[i + 1] == figur[i + 2] == figur[i + 3]:
            ergebnis = 7 #Vierling
            #print("Vierling")
            return ergebnis

    for i in range(len(figur) - 4):  # 0,1
        if (figur[i] == figur[i + 1] == figur[i + 2] and figur[i + 3] == figur[i + 4]) or (figur[i] == figur[i + 1] and figur[i + 2] == figur[i + 3] == figur[i + 4]):
            ergebnis = 6 #Full House
            #print("Full House")
            return ergebnis

    for i in range(len(farbe) - 4):  # 0
        if farbe[i] == farbe[i + 1] == farbe[i + 2] == farbe[i + 3] == farbe[i + 4]:
            ergebnis = 5 #Flush
            #print("Flush")
            return ergebnis

    for i in range(len(figur) - 4):  # 0
        if figur[i] == figur[i + 1] - 1 == figur[i + 2] - 2 == figur[i + 3] - 3 == figur[i + 4] - 4:
            ergebnis = 4 #Straße; Aktuell OHNE übers eck (z.b. Junge - Dame - Ass - 2 - 3)
            #print("Straße")
            return ergebnis

    for i in range(len(figur) - 2):  # 0,1,2
        if figur[i] == figur[i + 1] == figur[i + 2]:
            ergebnis = 3 #Drilling
            #print("Drilling")
            return ergebnis

    for i in range(len(figur) - 1): #0,1,2,3
        if figur[i] == figur[i + 1]: # [0,0,2,4,4]
            if i == 0:
                if figur[i + 2] == figur[i + 3] or figur[i + 3] == figur[i + 4]:
                    ergebnis = 2 #2x Paar
                    #print("2x Paare")
                    return ergebnis
            elif i == 1:
                if figur[i + 2] == figur[i + 3]:
                    ergebnis = 2 #2x Paar
                    #print("2x Paare")
                    return ergebnis

            ergebnis = 1 #Paar
            #print("Paar")
            return ergebnis
    ergebnis = 0
    #print("Hohe Karte")
    return ergebnis


if __name__ == '__main__':
    main()