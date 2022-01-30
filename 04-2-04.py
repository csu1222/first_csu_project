charcter = {
    "name": "기사",
    "level": 12,
    "item": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"},
    "skill": ["베기", "세게 베기","아주 세게 베기"]
    }


for key in charcter:
    if type(charcter[key]) is dict:
        for i in charcter[key]:
            print(key, ": ", charcter[key][i])
    elif type(charcter[key]) is list:
        for item in charcter[key]:
            print(key, ": ", item)
    else:
        print(key, ": ", charcter[key])