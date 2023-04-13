# 프로그래머스 Lv 1. 쉬운 시뮬레이션형 문제
# 주의 할 점, 지나갈 수 있는 곳인지 아닌지는 그냥 벽을 근거로 논리연산자를 쓰자.
# 아래 코드처럼 O or S 이런 식으로 하니까 헷갈리고 시간 잡어먹는다.

def solution(park, routes):    
    direct = {'E' : (0,1) , 'W' : (0,-1) , 'S' : (1,0), 'N' : (-1,0)}
    N,M = len(park),len(park[0]) # 세로,가로
    
    flag = 0
    for col in range(N):
        if flag:
            break
        for row in range(M):
            if park[col][row] == 'S':
                sy,sx = col,row
                flag = 1
                break
    
    loc = [(sy,sx)]
    temp = []
    flag = 0
    for idx in routes:
        cnt = 0
        info = idx.split()
        d,s = info[0],int(info[1])
        
        for i in range(1,s+1):
            ny = sy+direct[d][0]
            nx = sx+direct[d][1]
            if 0<=ny<N and 0<=nx<M and (park[ny][nx] == 'O' or park[ny][nx] == 'S'):
                flag = 0
                sy,sx = ny,nx
                temp.append((sy,sx))
                cnt+=1

            elif not (0<=ny<N and 0<=nx<M) or park[ny][nx] == 'X':
                flag = 1
                sy,sx = loc[-1][0],loc[-1][1]
                temp.clear()
                break
        
        loc.extend(temp)
        temp.clear()
    
    return sy,sx
