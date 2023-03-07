def solution(N, stages):
    stages.sort(reverse=True)
    answer = []
    rank = 1
    order = 1
    while len(stages)>=1:
        cnt,cnt2 = 0,0
        for idx in range(len(stages)-1,-1,-1): # 스테이지 싸악 훑자
            if stages[idx] > rank: # 이미 다음 스테이지인 경우
                cnt2+=1
            if stages[idx] == rank: # 스테이지에 머물러있는 경우
                cnt+=1
        
        for idx in range(cnt): # 스테이지에 머물러있는 유저 수만큼
            stages.pop() # 나가리~
            
        result = cnt/(cnt+cnt2)
        answer.append([order,result])
        rank+=1
        order+=1
    
    real = sorted(key, lambda x : x[0], -x[1])
        
    return real
  
  
  ######################## 아래는 내가 시도하려했던 풀이와 유사한 다른 분의 정답 코드. 분석 필요 ###############
#   def solution(N, stages):
#     failure_rate = {}
#     stages_len = len(stages)

#     for i in range(1, N+1):
#         if stages_len != 0:
#             stage_count = stages.count(i)
#             failure_rate[i] = stage_count/stages_len
#             stages_len -= stage_count
#         else:
#             failure_rate[i] = 0

#     answer = sorted(failure_rate.keys(), key=lambda key: failure_rate[key], reverse=True)

#     return answer
