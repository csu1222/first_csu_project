with open("wtitelines_test.txt", "w") as f:
    f.writelines(["첫째줄",
        "줄바꿈이 되나",
        "안되나",
        "띄어쓰기가 되나"])

    f.writelines([True, 123, "str"])