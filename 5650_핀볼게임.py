from collections import*

dd=[(-1,0),(0,1),(1,0),(0,-1)]
def bfs(r, c, dir):
    q=deque()
    q.append((r, c, dir,0))
    while q:
        x, y, d, cnt = q.popleft()
        dx, dy = dd[d]
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]==5:
            q.append((x, y, (d+2)%4, cnt+1 ))  #뒤로돌아
        elif mem[nx][ny][d] != -1: return cnt + mem[nx][ny][d]
        elif a[nx][ny] == -1: return cnt
        elif a[nx][ny] == 1:
            if d == 2:
                q.append((nx, ny, 1, cnt+1))
            elif d == 3:
                q.append((nx, ny, 0, cnt+1))
            else:
                q.append((x, y, (d+2)%4, cnt+1))
        elif a[nx][ny] == 2:
            if d == 0:
                q.append((nx, ny, 1, cnt+1))
            elif d == 3:
                q.append((nx, ny, 2, cnt+1))
            else:
                q.append((x, y, (d+2)%4, cnt+1))
        elif a[nx][ny] == 3:
            if d == 1:
                q.append((nx, ny, 2, cnt+1))
            elif d == 0:
                q.append((nx, ny, 3, cnt+1))
            else:
                q.append((x, y, (d+2))%4, cnt+1)
        elif a[nx][ny] == 4:
            if d == 1:
                q.append((nx, ny, 0, cnt+1))
            elif d == 2:
                q.append((nx, ny, 3, cnt+1))
            else:
                q.append((x, y, (d+2)%4, cnt+1))
        elif 6 <= a[nx][ny] <= 10:  #웜홀
            for tx, ty in warm[a[nx][ny]]:
                if tx==nx and ty==ny:continue
                q.append((tx, ty, d, cnt))
        else:
            q.append((nx, ny, d, cnt))

for t in range(int(input())):
    res, temp = 0, 0
    n=int(input())
    warm = [[]for _ in range(11)]
    a=[]
    for i in range(n):
        a.append(list(map(int,input().split())))
        for j in range(n):
            if 6<= a[i][j] <=10:
                warm[a[i][j]].append((i,j))
    mem=[[[-1]*4 for _ in range(n)]for _ in range(n)]  #memoization
    for i in range(n):
        for j in range(n):
            if not a[i][j]:     #빈곳이고
                for k in range(4):
                    if mem[i][j][k]==-1:    #방문 안한 곳(방향도)
                        temp = bfs(i, j, k)
                        mem[i][j][k]=temp
                    res = max(res, temp)
    print(res)
