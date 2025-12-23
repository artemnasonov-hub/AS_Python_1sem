if __name__ == "__main__":
    pass





def MtrProd(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])
    result = []
    for i in range(rows_A):
        row = []
        for j in range(cols_B):
            row.append(0)
        result.append(row)
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

#пример матриц
A = [
    [5, 2],
    [7, 4] ]


B = [
    [1, 2],
    [3, 4] ]


C = MtrProd(A, B)

print("A:")
for row in A:
    print(row)

print("\n B:")
for row in B:
    print(row)

print("\nПроизведение :")
for row in C:
    print(row)
