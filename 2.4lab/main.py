if __name__ == "__main__":
    pass




def filter_items(items, condition=None):
    if condition is None:
        return items
    result = []
    for item in items:
        if condition(item):
            result.append(item)
    return result



def merge_and_filter(list1, list2, filter_function=None):
    merged = []
    for x in list1:
        merged.append(x)
    for x in list2:
        merged.append(x)
    if filter_function is None:
        return merged
    result = []

    for item in merged:
        if filter_function(item):
            result.append(item)
    return result


def common_in_all(*lists):
    if len(lists) == 0:
        return []
    result = []

    for item in lists[0]:
        found_in_all = True

        for i in range(1, len(lists)):
            if item not in lists[i]:
                found_in_all = False
                break

        if found_in_all and item not in result:
            result.append(item)

    return result

def find_primes(*numbers):
    result = []

    for num in numbers:
        if num < 2:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            result.append(num)
    return result



print("а) filter_items")
print(filter_items([1, 2, 3, 4, 5]))
print(filter_items([1, 2, 3, 4, 5], condition=lambda x: x > 3))

print("\nб) merge_and_filter")
print(merge_and_filter([1, 2], [3, 4]))
print(merge_and_filter([1, 2], [3, 4], filter_function=lambda x: x % 2 == 0))

print("\nв) common_in_all")
print(common_in_all([1, 2, 3], [2, 3, 4], [3, 4, 5]))
print(common_in_all(['яблоко', 'вишня'], ['виноград', 'вишня'], ['вишня', 'дыня']))

print("\nг) find_primes")
print(find_primes(2, 3, 4, 5, 6, 7))
print(find_primes(10, 15, 17, 19, 23))
