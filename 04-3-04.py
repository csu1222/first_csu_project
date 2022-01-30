max_value = 0
a = 0
b = 0

for i in range(1, 100 // 2 +1):
    j = 100 - i

    # 최댓값 구하기
    a = i
    b = j
    max_value = a * b
    max_value_before = (a -1) * (b +1)
    if max_value > max_value_before:
        continue
    else:
        break



print("최대가 되는 경우: {} * {} = {}".format(a, b, max_value))