def find_min(numbers):
    min_number = None
    for number in numbers:
        if  (min_number is None) or (number < min_number):
            min_number = number
    print(f"Минимальное число в списке {numbers}:  {min_number}")

find_min([5, 7, 3, 1, 0])