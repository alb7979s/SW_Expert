def solve(pos, cnt):
    global a
    res = INF
    if cnt >= k: return cnt
    if pos == n:
        if check(): return cnt
        return res
    b = [x[:] for x in a]
    res = min(res, solve(pos+1, cnt))
    paint(pos, 0)
    res = min(res, solve(pos+1, cnt+1))
    paint(pos, 1)
    res = min(res, solve(pos+1, cnt+1))
    a = [x[:] for x in b]
    return res

def paint(pos, c):
    for i in range(m):
        a[pos][i] = c

def check():
    for i in range(m):
        c = 1; temp =1
        for j in range(n-1):
            if a[j][i] != a[j+1][i]:
                c=1
            else: c+=1
            temp = max(temp, c)
        if temp < k: return 0
    return 1
INF=1e9
for t in range(int(input())):
    n, m, k = map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    print('#{} {}'.format(t+1, solve(0,0)))
