if __name__ == "__main__":
    pass


f = open("f.txt", "w", encoding="utf-8")
f.write("1\n-3\n4\n-2\n5\n-6\n")
f.close()

f = open("f.txt", "r", encoding="utf-8")
numbers = []

for line in f:
    numbers.append(int(line))

f.close()

positive = []
negative = []

for num in numbers:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)


g = open("g.txt", "w", encoding="utf-8")

for i in range(len(positive)):
    g.write(str(positive[i]) + "\n")
    g.write(str(negative[i]) + "\n")

g.close()


print("Содержимое файла f.txt:")
f = open("f.txt", "r", encoding="utf-8")
print(f.read())
f.close()

print("Содержимое файла g.txt:")
g = open("g.txt", "r", encoding="utf-8")
print(g.read())
g.close()
