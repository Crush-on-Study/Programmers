# 프로그래머스 Lv2.
# 슬라이딩윈도우 + set으로 시간초과를 아슬아슬하게 피한 듯 하다.
# 더 효율적인게 있을까..?

def solution(elements):
    answer = set()
    leng = len(elements)
    index = 1
    for index in range(1,leng+1):
        for idx in range(0,leng):
            if idx+index <= leng:
                answer.add(sum(elements[idx:idx+index]))
            elif idx+index > leng:
                check = idx+index-leng
                answer.add( (sum(elements[idx:leng]))+(sum(elements[0:check])) )
    return len(answer)
