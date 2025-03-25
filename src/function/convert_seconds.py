def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes

def print_conversion(seconds):
    hours, minutes = convert_seconds(seconds)
    print((hours, minutes))
    print(f"В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы).")

print_conversion(23456)


