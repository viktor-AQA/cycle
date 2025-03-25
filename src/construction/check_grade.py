def check_grade(score):
    try:
        if score > 100 or score < 0:
            raise ValueError("Введите число от 0 до 100")
        elif 100 <= score <= 90:
            print("Отлично")
        elif 89 <= score <= 75:
            print("Хорошо")
        elif 74 <= score <= 50:
            print("Удовлетворительно")
        elif 0 <= score < 50:
            print("Неудовлетворительно")
    except ValueError as error:
        print(error)

check_grade(-5)
