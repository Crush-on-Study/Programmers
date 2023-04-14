# 프로그래머스 Lv 1
def solution(lottos, win_nums):
    cnt,cnt0 = 0,0
    for idx in lottos: # 내가 산거
        if not idx: # 0이면
            cnt0+=1
        else:
            for jdx in win_nums:
                if idx == jdx:
                    cnt +=1
    answer = []       
    max_check = cnt+cnt0
    min_check = cnt
    
    dic = {6:1 , 5:2, 4:3 , 3:4 , 2:5}
    if max_check >= 2:
        answer.append(dic[max_check])
    
    if max_check < 2:
        answer.append(6)
        
    if min_check >= 2:
        answer.append(dic[min_check])
        
    if min_check < 2:
        answer.append(6)
    
    return answer
