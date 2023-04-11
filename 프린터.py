# 백준 실버3 프린터 큐 / 프로그래머스 Lv 2 프린터
from collections import deque
def solution(priorities, location):
    answer = 0
    pq = deque(priorities)
    place = [i for i in range(len(priorities))]
    lq = deque(place)

    max_check = max(pq)

    cnt = 0 # 몇번째임?
    while pq:
        if pq[0] == max_check:
            pq.popleft()
            answer = lq.popleft()
            cnt+=1
            if pq:
                max_check = max(pq) # 다음 최우선순위는 무엇인지?
            if answer == location: # 만약 원하던 순서랑 만나면
                break

        elif pq[0] != max_check:
            temp = pq.popleft()
            temp2 = lq.popleft()
            pq.append(temp)
            lq.append(temp2)

    return cnt
