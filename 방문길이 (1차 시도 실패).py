# 틀린 풀이다. 엣지케이스 잡다 시간 다 

def solution(dirs):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    d = ['R','U','L','D'] # 동 북 서 남
    
    x,y = 0,0
    cnt,mul = 0,0
    arr = [(x,y)]
    for i in dirs:
        for idx in range(4):
            if i==d[idx]:
                nx = x+dx[idx]
                ny = y+dy[idx]
                if -5<=nx<=5 and -5<=ny<=5:
                    if (nx,ny) not in arr:
                        x,y = nx,ny
                        arr.append((x,y))
                        cnt+=1
                    elif (nx,ny) in arr:
                        x,y = nx,ny
                        arr.append((x,y))
                        mul+=1
                        cnt+=1
                        
    if mul==1:
        return cnt
    
    elif mul==0:
        return cnt
    
    else:
        return cnt-mul+1
