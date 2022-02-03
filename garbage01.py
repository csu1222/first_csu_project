# 가비지 컬렉터 : 변수에 저장 하지 않는 경우
from cgi import print_environ


class Test:
    def __init__(self, name):
        self.name = name
        print("{} - 생성되었습니다.".format(self.name))

    def __del__(self):
        print("{} - 파괴되었습니다.".format(self.name))


Test("A")
Test("B")
Test("C")
