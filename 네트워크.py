# 프로그래머스 Lv 3.
# 인접행렬을 인접리스트로 바꿔서 DFS로 연결요소 개수를 구하는 것이었다.
# 인접행렬로 연결요소 개수를 구하려고 플러드필을 썼었는데, 틀린 풀이가 되길래 인접리스트로 바꿨는데 통과했다.
# 이유를 찾아보자.

cnt = 0
def solution(n, computers):
    global cnt
    graph = [[] for _ in range(n)]    
    loc = []
    for i in range(n):
        for j in range(n):
            if computers[i][j] and i!=j:
                loc.append((i,j))

    for idx in range(len(loc)):
        a,b = loc[idx]
        graph[a].append(b)
        graph[b].append(a)

    visited = [0]*n

    arr = []
    def dfs(start):
        global cnt
        for next in graph[start]:
            if not visited[next]:
                visited[next] = 1
                cnt += 1
                dfs(next)

        return cnt

    cnt = 1

    arr = []
    while sum(visited) != n:
        for idx in range(len(visited)):
            if not visited[idx]:
                visited[idx] = 1
                result = dfs(idx)
                arr.append(result)

    return len(arr)
