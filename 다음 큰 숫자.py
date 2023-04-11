# 프로그래머스 Lv2
# 나는 이렇게했지만 다른 사람 풀이보니까 count라는 메서드로 손쉽게 푸는거 같다. 애용해보자.
def solution(n):
    b1 = bin(n)[2:]
    # print(b1)
    cnt,save = 0,0
    for idx in b1:
        if idx == '1':
            cnt+=1
    
    while True:
        check = 0
        n += 1
        for idx in bin(n)[2:]:
            save = n+1
            if idx == '1':
                check += 1
        if check == cnt:
            check = 0
            break
        
    return save-1
