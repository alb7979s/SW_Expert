from collections import*
def bfs(x, y):
    q=deque()
    q.append((x,y))
    check=[[0]*n for _ in range(n)]
    check[x][y]=1
    k=1;h=0;res=0
    if a[x][y]: h+=1
    while 1:
        if not q: break
        temp = h * m - (k ** 2 + (k - 1) ** 2)
        if temp>=0: res = max(res, h)
        k += 1
        for i in range(len(q)):
            x, y = q.popleft()
            for dx, dy in dd:
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>n-1 or ny>n-1 or check[nx][ny]: continue
                if a[nx][ny]: h+=1
                q.append((nx,ny))
                check[nx][ny]=1
    return res
dd=[(1,0),(0,1),(-1,0),(0,-1)]
for t in range(int(input())):
    n,m=map(int,input().split())    #n 정사각형 한변, m받는 돈
    a=[list(map(int,input().split()))for _ in range(n)]
    res=0
    for i in range(n):
        for j in range(n):
            res=max(res, bfs(i,j))
    print("#{} {}".format(t+1, res))
