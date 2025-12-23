if __name__ == "__main__":
    pass




file = open("matric.txt", "r", encoding="utf-8")
lines = file.readlines()
file.close()

matric = []
matrix = []

for line in lines:
    line = line.strip()
    if line == "":
        if matrix != []:
            matric.append(matrix)
            matrix = []
    else:
        row = list(map(int, line.split()))
        matrix.append(row)

if matrix != []:
    matric.append(matrix)
good_matric = []

for i in range(len(matric)):
    mat = matric[i]
    s = 0

    for row in mat:
        for x in row:
            if x > 0 and x % 2 == 0:
                s += x
    if s % 2 == 0:
        good_matric.append(mat)
        size = len(mat)
        new_mat = []
        for r in range(size):
            row = []
            for c in range(size):
                if r == c:
                    row.append(1)
                else:
                    row.append(0)
            new_mat.append(row)

        matric[i] = new_mat

out = open("even_sum_matric.txt", "w", encoding="utf-8")

for mat in good_matric:
    for row in mat:
        out.write(" ".join(map(str, row)) + "\n")
    out.write("\n")

out.close()

print("Содержимое  после замены :")
for mat in matric:
    for row in mat:
        print(row)
    print()

print("Матрицы с чётной :")
for mat in good_matric:
    for row in mat:
        print(row)
    print()
