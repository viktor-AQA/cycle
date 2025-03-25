def cycle():
    number = int(input("Введите число: "))
    numbers = []
    while number > 0:
        numbers.append(number)
        number -= 1
    print(f"Числа: {numbers}")
    result = 0
    for num in numbers:
        result += num
    print(f"Сумма чисел {result}")

cycle()