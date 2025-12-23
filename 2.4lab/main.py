if __name__ == "__main__":
    pass




def merge_lists_with(list1, list2, merge_function=None):
    if merge_function is None:
        return list1 + list2
    result = []
    for x, y in zip(list1, list2):
        result.append(merge_function(x, y))
    return result
def extract_digits(strings, digits_only=False):
    if not digits_only:
        return strings
    result = []
    for text in strings:
        digits = ""
        for symbol in text:
            if symbol.isdigit():
                digits += symbol
        result.append(digits)
    return result

def filter_even_numbers(*numbers):
    result = []

    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result



def sorted_positive_numbers(*numbers):
    positive_numbers = []

    for num in numbers:
        if num > 0:
            positive_numbers.append(num)

    positive_numbers.sort(reverse=True)

    return positive_numbers



# Проверка работы функций


print("а) merge_lists_with")
print(merge_lists_with([1, 2], [3, 4]))
print(merge_lists_with([1, 2], [3, 4], merge_function=lambda x, y: x + y))

print("\nб) extract_digits")
print(extract_digits(['a1b2', 'c3d4']))
print(extract_digits(['a1b2', 'c3d4'], digits_only=True))

print("\nв) filter_even_numbers")
print(filter_even_numbers(1, 2, 3, 4, 5, 6))
print(filter_even_numbers(7, 9, 11))

print("\nг) sorted_positive_numbers")
print(sorted_positive_numbers(-1, 3, -5, 7, 0))
print(sorted_positive_numbers(-10, -20))
