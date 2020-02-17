from collections import*

dd=[(-1,0),(0,1),(1,0),(0,-1)]
def bfs(r, c, dir):
    q=deque()
    q.append((r, c, dir, 0))
    while q:
        x, y, d, cnt = q.popleft()
        dx, dy = dd[d]
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]==5:        #nx, ny 일관되게 안넣고 x, y 넣었다가 잘못되었었음
            q.append((nx, ny, (d+2)%4, cnt+1 ))  #뒤로돌아
        elif d != dir and (x ==i and y ==j): return cnt
        elif a[nx][ny] == -1 or (nx == i and ny == j): return cnt
        elif a[nx][ny] == 1:
            if d == 2:
                q.append((nx, ny, 1, cnt+1))
            elif d == 3:
                q.append((nx, ny, 0, cnt+1))
            else:
                q.append((nx, ny, (d+2)%4, cnt+1))
        elif a[nx][ny] == 2:
            if d == 0:
                q.append((nx, ny, 1, cnt+1))
            elif d == 3:
                q.append((nx, ny, 2, cnt+1))
            else:
                q.append((nx, ny, (d+2)%4, cnt+1))
        elif a[nx][ny] == 3:
            if d == 1:
                q.append((nx, ny, 2, cnt+1))
            elif d == 0:
                q.append((nx, ny, 3, cnt+1))
            else:
                q.append((nx, ny, (d+2)%4, cnt+1))
        elif a[nx][ny] == 4:
            if d == 1:
                q.append((nx, ny, 0, cnt+1))
            elif d == 2:
                q.append((nx, ny, 3, cnt+1))
            else:
                q.append((nx, ny, (d+2)%4, cnt+1))
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
    for i in range(n):
        for j in range(n):
            if not a[i][j]:     #빈곳이고
                for k in range(4):           #메모이제이션 할랬는데 웜홀때문에 숫자 중첩 되어서 잘못되었었음(끝나는 곳 다르잖아)
                    temp = bfs(i, j, k)
                    res = max(res, temp)
    print('#{} {}'.format(t+1,res))
