if __name__ == "__main__":
    pass




first = {1: 2, 3: 4, 5: 6}
second = {1: 3, 3: 4}
print("а) Элементы:")

for key in first:
    print(key, ":", first[key])
values = []
for key in first:
    values.append(first[key])
values.sort(reverse=True)
three = values[:3]
print("\nб) Три наибольших значения:")
print(three)
result = {}

for key in first:
    if key in second:
        result[key] = (first[key], second[key])
print("\nв) Сопоставление :")
print(result)
