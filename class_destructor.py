# 소멸자 예제
class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))


test = Test("A")
