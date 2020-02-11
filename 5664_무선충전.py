#charge 만드는 부분 잘못되었
dd=[(0,0),(-1,0),(0,1),(1,0),(0,-1)]
for t in range(int(input())):
    charge=[[[]for _ in range(10)] for _ in range(10)]
    m, c = map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for i in range(c):
        x, y, k, p = map(int,input().split())
        x-=1; y-=1
        charge[x][y].append(p)
        check=[[0]*10 for _ in range(10)]
        check[x][y]=1
        for dx, dy in dd[1:]:
            nx, ny =x, y
            for j in range(k):
                nx, ny = nx+dx, ny+dy
                if nx<0 or ny<0 or nx>9 or ny>9: break
                if not check[nx][ny]:charge[nx][ny].append(p)
    for i in range(10):
        for j in range(10):
            if charge[nx][ny]:
                charge[nx][ny].sort(reverse=True)
    sx, sy = 0, 0
    ex, ey = 9, 9
    res=0
    if charge[0][0]: res+=charge[0][0][0]
    if charge[-1][-1]: res+=charge[-1][-1][0]
    for i in range(m):  #이동
        dsx, dsy = dd[a[i]]
        dex, dey = dd[b[i]]
        sx, sy = sx+dsx, sy+dsy
        ex, ey = ex+dex, ey+dey
        if sx==ex and sy==ey and charge[sx][sy]:
            if len(charge[sx][sy])==1: res += (charge[sx][sy][0])
            else: res += charge[sx][sy][0] + charge[sx][sy][1]
        else:
            if charge[sx][sy]: res+=charge[sx][sy][0]
            if charge[ex][ey]: res+=charge[ex][ey][0]
    for i in range(10):
        for j in range(10):
            if charge[i][j]: print(i,j)
    print("#{} {}".format(t+1, res))
