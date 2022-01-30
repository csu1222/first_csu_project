min_sit = 2
max_sit = 10
total = 100
memo = {}

def sit_pro(remain, sit):
    key = str([remain, sit])
    # 종료 조건
    if key in memo:
        return memo[key]
    if remain < 0:
        return 0     # 무효이므로 0을 리턴
    if remain == 0:
        return 1    # 유효하므로 수를 세기위해 1을 리턴
    # 재귀 처리
    count = 0
    for i in range(sit, max_sit + 1):
        count += sit_pro(remain - i, i)
    # 메모화 처리
        memo[key] = count
    # 종료
    return count
print(sit_pro(total, min_sit))

# 실행결과 437420