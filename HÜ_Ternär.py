def main():
    daten = {
        "A": (1, 2),
        "B": (3, 4)
    }
    wahl = "A"
    ternär(daten, wahl)

def ternär(daten, wahl):
    ergebnis = daten[wahl] if wahl in daten else (0, 0)

    print(ergebnis)

if __name__ == "__main__":
    main()