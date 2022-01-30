numbers  = [1, 2, 5, 7, 9, 5, 3, 1, 4, 5, 6 ,8 ,7, 5]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] = counter[number] + 1
    else:
        counter[number] = 1



print(counter)