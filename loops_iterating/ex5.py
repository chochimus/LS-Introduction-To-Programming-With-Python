my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for arr in my_list:
    for num in arr:
        if num % 2 == 0:
            print(num)