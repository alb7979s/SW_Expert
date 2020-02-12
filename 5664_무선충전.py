#구역들 귀찮아서 p로 체크했다가 틀림(데이터 p 같은경우 때문에)
from collections import* #p 같은 경우 틀림
dd=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]
def solve(a, b):
    res=0
    if a and b:
        for i in range(len(a)):
            for j in range(len(b)):
                if a[i][0] == b[j][0]:  # idx 같은 경우
                    res = max(res, a[i][1])
                else:
                    res = max(res, a[i][1]+b[j][1])
    if a and (not b):return sorted(a, key = lambda x: x[1])[-1][1]
    if b and (not a):return sorted(b, key = lambda x: x[1])[-1][1]
    return res
for t in range(int(input())):
    charge=[[[]for _ in range(10)] for _ in range(10)]
    m, c = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(c):
        y, x, k, p = map(int,input().split())
        x-=1; y-=1
        charge[x][y].append([i,p])
        check=[[0]*10 for _ in range(10)]
        check[x][y] = 1
        q = deque()
        q.append((x, y,0))
        while q:
            x, y, c = q.popleft()
            if c==k: break
            for dx, dy in dd[1:]:
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>9 or ny>9 or check[nx][ny]:continue
                q.append((nx,ny,c+1))
                check[nx][ny]=1
                charge[nx][ny].append([i,p])

    sx, sy = 0, 0
    ex, ey = 9, 9
    res=solve(charge[sx][sy],charge[ex][ey])
    for i in range(m):  #이동
        dsx, dsy = dd[a[i]]
        dex, dey = dd[b[i]]
        sx, sy = sx+dsx, sy+dsy
        ex, ey = ex+dex, ey+dey
        res += solve(charge[sx][sy], charge[ex][ey])
    print("#{} {}".format(t+1, res))
