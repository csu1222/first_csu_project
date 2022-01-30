# 함수 선언
def test():
    print("A pass")
    yield 1
    print("B pass")
    yield 2
    print("C pass")

# 함수 호출
output = test()
# next() 함수 호출
print("D pass")
a= next(output)
print(a)
print("E pass")
b=next(output)
print(b)
print("F pass")
c=next(output)
print(c)

# 한 번 더 실행
next(output)
