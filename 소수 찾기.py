import math
def solution(numbers):
    box = []
    answer = 0
    arr = [idx for idx in numbers]
    arr2 = []
    visited = [False]*len(numbers)
    
    def back(num,idx):
        if num==idx:
            box.append(''.join(map(str,arr2)))
            return
        
        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                arr2.append(arr[i])
                back(num+1,idx)
                visited[i] = False
                arr2.pop()
        return box
    
    for idx in range(1,len(arr)+1):
        result = back(0,idx)
    
    int_box = set()
    for idx in result:
        if idx[0] == '0':
            int_box.add(int(idx[-1]))
        else:
            int_box.add(int(idx))
    
    int_box = list(int_box)
    
    n = max(int_box)
    arr3 = [True for i in range(n+1)]
    arr3[0] = False
    arr3[1] = False
    for i in range(2,int(math.sqrt(n))+1):
        if arr3[i] == True:
            j = 2
            while i*j <= n:
                arr3[i*j] = False
                j+=1
    
    for idx in int_box:
        if arr3[idx]:
            answer+=1
    
    return answer
