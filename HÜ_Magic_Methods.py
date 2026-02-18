class Auto:
    def __init__(self, ps):
        self.ps = ps

    def _check(self, other):
        if not isinstance(other, Auto):
            raise TypeError("nur Auto Objekte erlaubt")

    def __len__(self):
        return self.ps

    def __add__(self, other):
        self._check(other)
        return self.ps + other.ps

    def __sub__(self, other):
        self._check(other)
        return self.ps - other.ps

    def __mul__(self, other):
        self._check(other)
        return self.ps * other.ps

    def __eq__(self, other):
        self._check(other)
        return self.ps == other.ps

    def __lt__(self, other):
        self._check(other)
        return self.ps < other.ps

    def __gt__(self, other):
        self._check(other)
        return self.ps > other.ps

def main():
    a1 = Auto(50)
    a2 = Auto(60)
    a3 = Auto(50)

    print(len(a1))
    print(a1 + a2)
    print(a1 - a2)
    print(a1 * a2)
    print(a1 == a3)
    print(a1 == a2)
    print(a1 < a2)
    print(a1 > a2)

if "__main__" == __name__:
    main()