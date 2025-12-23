if __name__ == "__main__":
    pass




def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


# Проверка работы функции
N = int(input("Введите натуральное число: "))
print("Сумма цифр:", sum_of_digits(N))
