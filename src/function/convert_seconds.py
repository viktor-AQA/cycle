def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    print((hours, minutes))
    print(f"В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы).")


convert_seconds(23456)

