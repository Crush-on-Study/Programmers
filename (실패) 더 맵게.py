# 대체 뭘 어쩌란거지 왜 자꾸 인덱스 에러 쳐나는데
import heapq
def solution(scoville, K):
    answer = 0
    q = []
    for idx in scoville:
        heapq.heappush(q,idx)
    need = 0
    
    if len(q)>1:
        while True:
            first = heapq.heappop(q)
            if first >= K:
                return need
            second = q[0]
            #print(second)
            make = first + second*2
            heapq.heappush(q,make)
            #print(q)
            heapq.heappop(q)
            #print(q)
            need+=1
            
    elif len(q)==1 and q[0]<K:
        return -1
        
    return -1
