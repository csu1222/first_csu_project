# 모듈을 읽어들입니다.
from math import frexp


from primePy import primes


def prime_to_len(start, end):
    global primes

    output_end = (primes.upto(end))
    output_start = (primes.upto(start))

    for item in output_start:
        output_end.remove(item)
    str_list = map(str, list(output_end))
    ed = "".join(str_list)
    return len(output_end)


print(prime_to_len(100, 1000))
