def count_vowels(str1):
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in str1:
        if char in vowels:
            count += 1
    return str1, count

string_input = "My name is Antonio"
str1, count = count_vowels(string_input)

print(f"Количество гласных в строке '{str1}': {count}")