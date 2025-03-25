def greet_user():
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}! Добро пожаловать в мир Python!")

def calculate_sum():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a + b
    return result

greet_user()
print(f"Сумма чисел: {calculate_sum()}")
