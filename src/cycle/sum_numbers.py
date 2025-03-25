def print_diamond(rows):

    for i in range(rows + 1):
        stars = '* ' * i
        print(stars)


    for i in range(rows - 1, 0, -1):
        stars = '* ' * i
        print(stars)


print_diamond(4)
