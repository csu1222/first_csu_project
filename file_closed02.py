# try except 구문
try:
    # 파일을 엽니다.
    file = open("info.txt", "w")
    # 여러가지 처리를 합니다
    예외.발생해라()
    # 파일 닫습니다
    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)