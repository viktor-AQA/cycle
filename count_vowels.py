def count_vowels(string):
    vowels = "aeiouyAEIOUY"

    count = 0
    for char in string:
        if char in vowels:
            count += 1
    print(f"Количество гласных в строке {string}: {count}")


count_vowels("My name is Antonio")
