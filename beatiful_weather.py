# 모듈을 읽어 들입니다.
from urllib import request
from bs4 import BeautifulSoup

# urlopen() 함수로 기상청의 전국 날씨를 읽습니다.
# 이 코드는 한줄 코드이니 이어서 입력해야 합니다
target = request.urlopen(
    "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeautifulSoup을 사용해 웹페이지를 분석 합니다.
soup = BeautifulSoup(target, "html.parser")

# location 태그를 찾습니다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, 태그를 찾아 출력합니다.
    print("도시:", location.select_one("city").string)
    print("날씨:", location.select_one("wf").string)
    print("최저기온:", location.select_one("tmn").string)
    print("최고기온:", location.select_one("tmx").string)
    print()