def solve(x, y, d, cnt):
    res = 0
    if d>3: return 0
    if scope(x, y): return 0
    if x == sx and y==sy: return cnt
    if a[x][y] in temp: return 0
    else: temp.append(a[x][y])
    res = max(res, solve(x+dd[d][0], y+dd[d][1], d, cnt+1), solve(x+dd[d+1][0],y+dd[d+1][1], d+1, cnt+1))
    temp.pop()
    return res
dd=[(1,1), (-1,1), (-1,-1), (1,-1), (0,0)]
def scope(nx, ny):
    if nx<0 or ny<0 or nx>n-1 or ny>n-1: return 1
    return 0
for t in range(int(input())):
    n = int(input())
    a=[list(map(int,input().split()))for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            temp=[a[i][j]]
            sx , sy = i, j
            ans = max(ans, solve(i+dd[0][0], j+dd[0][1], 0, 1))
    print('#{} {}'.format(t+1, ans if ans!=0 else -1))
