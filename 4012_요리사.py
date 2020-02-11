def solve(cnt, pos):
    res = INF
    if cnt>n//2: return res
    if pos == n:
        if cnt == n//2:
            res = min(res, cal())
        return res
    temp[pos]=1
    res=min(res, solve(cnt+1, pos+1))
    temp[pos]=0
    res=min(res, solve(cnt, pos+1))
    return res
def cal():
    ans=0;ans2=0
    for i in range(n):
        for j in range(n):
            if temp[i] and temp[j]:
                ans += a[i][j]
            elif not temp[i] and not temp[j]:
                ans2 += a[i][j]
    return abs(ans2-ans)
INF=1e9
for t in range(int(input())):
    n=int(input())
    temp=[0]*n
    a=[list(map(int,input().split()))for _ in range(n)]
    print("#{} {}".format(t+1,solve(0,0)))
