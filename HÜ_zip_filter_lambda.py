def main():
    names = ["Anna", "Bernd", "Claudia", "Dirk", "Eva"]
    ages = [23, 17, 34, 15, 29]
    scores = [88, 92, 75, 64, 91]

    # zu tuple machen
    zipped = zip(names, ages, scores)

    # nur personen mit alter >= 18 und einem score von >= 80
    filtered = filter(lambda t: t[1] >= 18 and t[2] >= 80, zipped)

    # tupel zu dictionary
    result = list(map(lambda t: {"name": t[0], "age": t[1], "score": t[2]}, filtered))

    print(result)

if __name__ == "__main__":
    main()