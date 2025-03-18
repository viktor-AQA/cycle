def sum_numbers(n):
    sum = 0
    for number in range(n + 1):
        sum += number
    print(f"Сумма чисел от 1 до {n}: {sum}")


sum_numbers(5)
