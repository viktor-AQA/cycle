def check_string_length(string, length):
    if len(string) > length:
        print("Длина строки достаточная")
    else:
        print("Строка слишком короткая")


check_string_length("string", 4)