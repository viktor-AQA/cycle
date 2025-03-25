def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(f"Сумма чисел от 1 до 5: {sum_numbers(5)}")
