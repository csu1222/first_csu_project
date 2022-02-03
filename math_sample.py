# 모듈을 가져옵니다.
from cgi import print_environ
import math

# 클래스를 선언합니다


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * (self.radius ** 2)


# 원의 둘레와 넓이를 구합니다.
circle = Circle(10)
print("원의 둘레:", circle.get_circumference())
print("원의 넓이:", circle.get_area())

# 하지만 radius 값에 음수를 넣으면 둘레가 음수가 나와 버리므로
# radius 값에 음수를 넣지 못하게 하는 방법이 필요
