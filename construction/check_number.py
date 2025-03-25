def check_number(number):
    if number > 0:
        if number % 2 == 0:
            print(f"Число {number} положительное и чётное.")
        else:
            print(f"Число {number} отрицательное или нечетное.")

check_number(7)