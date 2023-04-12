# 정말 무식한 방법이긴 한데 시간은 제일 빠를 듯 하다.
def solution(n, lost, reserve):
    answer = 0
    place = [1 for i in range(n)]

    for idx in range(len(lost)):
        place[lost[idx]-1] = 0

    for idx in range(len(reserve)):
        if place[reserve[idx]-1] == 0:
            place[reserve[idx]-1] = 1
        else:
            place[reserve[idx]-1] = 2

    for idx in range(n):
        if not place[idx] and idx == 0: # 제일 처음 애가 체육복 없는 경우
            if place[idx+1] == 2:
                place[idx]+=1
                place[idx+1]-=1

        elif not place[idx] and 0<idx<n-1: # 중간 애가 체육복 없는 경우
            if place[idx-1] == 2: 
                place[idx]+=1
                place[idx-1]-=1

            elif place[idx+1] == 2:
                place[idx]+=1
                place[idx+1]-=1

        elif not place[idx] and idx == n-1: # 제일 끝사람이 체육복 없는 경우
            if place[idx-1] == 2:
                place[idx]+=1
                place[idx-1]-=1

    for idx in place:
        if idx != 0:
            answer+=1

    return answer
