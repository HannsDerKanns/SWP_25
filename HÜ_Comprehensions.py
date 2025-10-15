import random

def main():
    listComprehension("oaire", "banane")

def listComprehension(buchstaben,word):
    listComp = [i+1 for i in range(len(buchstaben)) if buchstaben[i] in word]
    print(listComp)

def setComprehension():
    setComp = {random.randint(1, 10) for x in range(0, 8)}
    print(setComp)

def dictComprehension():
    dictComp = {number: "gerade" if number % 2 else "ungerade" for number in range(0, 20)}
    print(dictComp)

if __name__ == '__main__':
    main()