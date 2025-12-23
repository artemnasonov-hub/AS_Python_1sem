if __name__ == "__main__":
    pass
file = open("data.txt", "r", encoding="utf-8")
line = file.readline()
if line != "":
    parts = line.split()
    min_year = int(parts[2])
    for line in file:
        parts = line.split()
        year = int(parts[2])
        if year < min_year:
            min_year = year
    print("Наименьший год:", min_year)
else:
    print("Файл пустой")
file.close()
