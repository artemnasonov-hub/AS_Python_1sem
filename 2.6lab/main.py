if __name__ == "__main__":
    pass




def find_min_element(matrix):
    minimum = matrix[0][0]
    for row in matrix:
        for element in row:
            if element < minimum:
                minimum = element
    return minimum


def find_max_element(matrix):
    maximum = matrix[0][0]

    for row in matrix:
        for element in row:
            if element > maximum:
                maximum = element
    return maximum


def sum_of_elements(matrix):
    total_sum = 0

    for row in matrix:
        for element in row:
            total_sum += element
    return total_sum


def sum_of_row(matrix, row_number):
    row_sum = 0
    for element in matrix[row_number]:
        row_sum += element
    return row_sum



#пример
matrix = [
        [5, 7, 8],
        [9, 6, 4],
        [-1, 4, 2]
    ]

min_element = find_min_element(matrix)
max_element = find_max_element(matrix)
total_sum = sum_of_elements(matrix)
second_row_sum = sum_of_row(matrix, 1)

print("Матрица:")
for row in matrix:
    print(row)

print("Минимальный элемент:", min_element)
print("Максимальный элемент:", max_element)
print("Сумма всех элементов матрицы:", total_sum)
print("Сумма элементов 2-й строки:", second_row_sum)

