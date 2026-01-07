class Fahrzeug:
    def __init__(self, tires):
        self.tires = tires

    def fahren(self):
        print("Das Fahrzeug fährt.")


class Auto(Fahrzeug):
    def __init__(self, tires, ps):
        super().__init__(tires)
        self.ps = ps

    def info(self):
        print(f"{self.ps} PS; {self.tires} Reifen.")


class Cabrio(Auto):
    def __init__(self, tires, ps, no_roof):
        super().__init__(tires, ps)
        self.no_roof = no_roof

    def info(self):
        print(
            f"{self.ps} PS; {self.tires} Reifen; Dach offen: {self.no_roof}"
        )

def main():
    cabrio = Cabrio("Hankook", 150, True)
    cabrio.fahren()
    cabrio.info()

if __name__ == "__main__":
    main()