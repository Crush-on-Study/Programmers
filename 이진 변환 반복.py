# 프로그래머스 Lv2. 무난함
def solution(s):
    result = []
    cnt = 0
    cycle = 0
    while len(s)!=1:
        answer = []
        for idx in s:
            if idx == '1':
                answer.append(idx)
            else:
                cnt+=1
        s = str(bin(len(answer))[2:])
        cycle+=1
    
    result.append(cycle)
    result.append(cnt)
    return result
