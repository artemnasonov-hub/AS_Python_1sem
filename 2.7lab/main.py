if __name__ == "__main__":
    pass





K = int(input("Введите номер строки K: "))
file = open("te.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

if K >= 1 and K <= len(lines):
    del lines[K - 1]

file = open("te.txt", "w", encoding="utf-8")
for line in lines:
    file.write(line)
file.close()

print("Всё готово")
