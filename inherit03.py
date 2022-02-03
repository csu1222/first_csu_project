# 사용자 정의 예외 클래스 만들기
class CustomException(Exception):
    def __init__(self):
        Exception.__init__(self)
        print("### 내가 만든 오류가 생성되었어요! ###")

    def __str__(self):
        return "오류가 발생되었어요"


raise CustomException

# 부모 클래스에 원래 있던 함수를 다시 정의 하는것을 '오버라이드', '재정의' 라고 합니다.
