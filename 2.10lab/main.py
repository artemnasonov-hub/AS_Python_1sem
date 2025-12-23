if __name__ == "__main__":
    pass





file_name = input("Введите имя файла: ")

try:
    file = open(file_name, "r", encoding="utf-8")

    if not file_name.endswith(".txt"):
        raise TypeError("Файл не является текстовым")

    file.close()
    print("Файл успешно открыт")

except FileNotFoundError:
    print("Файл не найден")

except TypeError as error:
    print(error)

text = input("\nВведите строку: ")

try:

    number = float(text)
    print("Строка является числом")

except ValueError:
    raise Exception("Строка не является числом")


file_name = input("\nВведите имя файла для проверки через assert: ")

try:
    try:
        file = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        assert False, "Файл не найден"

    if not file_name.endswith(".txt"):
        raise TypeError("Файл не является текстовым")

    file.close()
    print("Файл успешно открыт")

except AssertionError as error:
    print(error)

except TypeError as error:
    print(error)
