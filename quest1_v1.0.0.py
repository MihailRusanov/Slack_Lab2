numbers = list(map(int, input().split()))
# numbers = [1, 2, 3, 1, 2, 5, 6, 7, 10, 10, 0, -4, -3, 12, 10]
# numbers.sort()

def get_unique_numbers(numbers):
    list_of_unique_numbers = []
    unique_numbers = set(numbers)

    for number in unique_numbers:
        list_of_unique_numbers.append(number)

    return list_of_unique_numbers


print(get_unique_numbers(numbers))
