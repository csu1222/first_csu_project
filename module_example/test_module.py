# test_module.py 파일
PI = 3.141592


def number_input():
    output = input("숫자 입력> ")
    return float(output)


def get_circumference(radius):
    return 2 * PI * radius


def get_circle_area(radius):
    return PI * radius * radius


# 예를 들어 이렇게 사용 됩니다.     # 현재 파일이 엔트리 포인트인지 확인하고, 엔트리 포인트 일 때만 실행합니다.
if __name__ == "__main__":
    print("# example")
    print("get_circumference(10):", get_circumference(10))
    print("get_circle_area(10):", get_circle_area(10))
