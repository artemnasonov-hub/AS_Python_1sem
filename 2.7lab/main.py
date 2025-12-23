if __name__ == "__main__":
    pass



file = open("input.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()
file = open("input.txt", "w", encoding="utf-8")

for line in lines:
    file.write(line)
    if line == "\n":
        file.write(line)
file.close()
