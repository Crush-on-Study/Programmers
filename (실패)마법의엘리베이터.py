def solution(storey):
    cnt,cnt2 = 0,0
    c = len(str(storey))-1 # 16일때, c는 1  9일 때, c는 0    
    ten = [10**i for i in range(c+1)]
    print(ten)
    min_check = (storey//(ten[-1]))*(ten[-1])
    max_check = (min_check+(ten[-1]))
    
    print(min_check,max_check)
    # 1
    temp = abs(max_check-storey)
    for i in range(len(ten)-1,-1,-1):
        cnt += temp//ten[i]
        print(cnt)
        temp = temp%ten[i]
    cnt += max_check//(ten[-1])
    
    # 2
    temp2 = abs(min_check-storey)
    for i in range(len(ten)-1,-1,-1):
        cnt2 += temp2//ten[i]
        temp2 = temp2%ten[i]
    cnt2 += min_check//ten[-1]
    
    answer = min(cnt,cnt2)
    return answer
