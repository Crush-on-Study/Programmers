# 프로그래머스 Lv2 2*n 타일링 / 백준 2*n 타일링 (실버)
# 왜 중간중간에 모듈연산해줘야 시간초과가 안나는걸까? return에다 모듈연산하면 시초나는데 왜지?
def solution(n):
    dp = [1,2]
    for i in range(1,n-1):
        dp.append((dp[i]+dp[i-1])%1000000007)
    return dp[-1]
