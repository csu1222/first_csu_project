# 파일을 엽니다.
file = open("basic.txt", "w")
# 파일에 텍스트를 씁니다.
file.write("Hello Python Pregramming...!")
# 파일을 닫습니다.
file.close()

# 파일을 엽니다
file = open("basic.txt", "r")
print(file.read())

file.close()
