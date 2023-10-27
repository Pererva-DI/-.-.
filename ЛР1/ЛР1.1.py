numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_without_none = numbers[:4] + numbers[5:]
average_of_numbers = sum(numbers_without_none) / len(numbers)
numbers[4] = average_of_numbers

print("Измененный список:", numbers)
