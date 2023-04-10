# 프로그래머스 Lv 2.
# 가로 개수가 4개로 고정되어서 그냥 DP문제라 생각했는데 문제 자체를 잘못 이해한 듯 하다. 다시해보자

def solution(land):
    max_check = 0
    max_check = max(max(land[0][0],land[0][1]),max(land[0][2],land[0][3]))
    answer = 0
    answer += max_check
    for idx in range(1,len(land)):
        if max_check == land[idx-1][0]:
            max_check = max(max(land[idx][1],land[idx][2]),land[idx][3])
            answer += max_check
            
        elif max_check == land[idx-1][1]:
            max_check = max(max(land[idx][0],land[idx][2]),land[idx][3])
            answer += max_check
        
        elif max_check == land[idx-1][2]:
            max_check = max(max(land[idx][0],land[idx][1]),land[idx][3])
            answer += max_check
            
        elif max_check == land[idx-1][3]:
            max_check = max(max(land[idx][0],land[idx][1]),land[idx][2])
            answer += max_check
            
    return answer
