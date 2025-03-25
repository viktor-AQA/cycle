def find_min(numbers):
    min = None
    for number in numbers:
        if  (min is None) or (number < min):
            min = number
    print(f"Минимальное число в списке {numbers}:  {min}")



find_min([5, 7, 3, 1, 0])