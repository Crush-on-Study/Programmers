# 프로그래머스 Lv2
from collections import deque
def solution(maps):
    n,m = len(maps),len(maps[0]) # 세로,가로    
    dx,dy= [1,0,-1,0],[0,1,0,-1]

    time = 0
    # 시작점,레버,도착점 찾기
    for col in range(n):
        for row in range(m):
            if maps[col][row] == 'S':
                sy,sx = col,row
            elif maps[col][row] == 'L':
                ly,lx = col,row
            elif maps[col][row] == 'E':
                ey,ex = col,row

    # 레버 찾으러가기
    def bfs(sy,sx):
        visited = [[-1]*m for _ in range(n)]
        q = deque()
        q.append((sy,sx))
        visited[sy][sx] = 0

        while q:
            sy,sx = q.popleft()
            for i in range(4):
                ny = sy+dy[i]
                nx = sx+dx[i]
                if 0<=ny<n and 0<=nx<m and visited[ny][nx] == -1:
                    if maps[ny][nx] == 'O' or maps[ny][nx] == 'E': 
                        visited[ny][nx] = visited[sy][sx]+1
                        q.append((ny,nx))

                    elif maps[ny][nx] == 'L':
                        return visited[sy][sx]+1

        return -1

    # after 레버
    def bfs2(ly,lx):
        visited = [[-1]*m for _ in range(n)]
        q = deque()
        q.append((ly,lx))
        visited[ly][lx] = 0

        while q:
            ly,lx = q.popleft()
            for i in range(4):
                ny = ly+dy[i]
                nx = lx+dx[i]
                if 0<=ny<n and 0<=nx<m and visited[ny][nx] == -1:
                    if maps[ny][nx] == 'S' or maps[ny][nx] == 'O':
                        visited[ny][nx] = visited[ly][lx]+1
                        q.append((ny,nx))

                    elif maps[ny][nx] == 'E':
                        return visited[ly][lx]+1

        return -1

    result = bfs(sy,sx)
    if result == -1:
        return -1

    else:
        result2 = bfs2(ly,lx)
        if result2 == -1:
            return -1
        else:
            time = time + result + result2
            return time
