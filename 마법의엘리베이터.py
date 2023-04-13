# 프로그래머스 Lv 2
# 굉장히 좋은 기법을 발견했다. 글 올려주신 분께 감사를!
def solution(storey):
    answer = 0
    while storey:
        remainder = storey % 10 # 6 -> 2
        # 6 ~ 9
        if remainder > 5:
            answer += (10 - remainder)  # 4만큼 카운팅
            storey += 10 # 26?
        # 0 ~ 4
        elif remainder < 5:
            answer += remainder # 2만큼 추가 카운팅
        # 5
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            answer += remainder
        storey //= 10  # 2

    return answer
