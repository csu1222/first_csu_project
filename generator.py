# 함수를 선언합니다.
def test():
    print("함수가 호출되었습니다.")
    yield "test"

# 함수를 호출
print("A지점 통과")
test()

print("B지점 통과")
print(test())