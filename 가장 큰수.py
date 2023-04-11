# 프로그래머스 Lv2 / 백준 플레5
# cmp_to_key는 언젠간 유용하게 쓰일 것

from functools import cmp_to_key # 대소비교, C++ class로 bool하는것과 유사함
def solution(numbers):
    numbers = [str(i) for i in numbers]
    def compare(x,y):
        if x+y > y+x: # 6,10있을 때 610 106이렇게 비교
            return -1 # 안바꿔진다는 뜻. x,y 순으로 유지
        elif x+y<=y+x:
            return 1 # 바꿔진다는 뜻. y,x 순으로 체인지

    numbers = sorted(numbers, key = cmp_to_key(compare))
    answer = ''
    for idx in numbers:
        answer+=idx

    if answer[0] == '0':
        return '0'

    return answer
