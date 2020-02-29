'''
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
'''
#이게 더 깔끔
from collections import*
dd=[(-1,0), (0,1), (1,0), (0, -1)]  #URDL
reflex=[[0,0,0,0],
        [2,3,1,0],      #1
        [1,3,0,2],      #2
        [3,2,0,1],      #3
        [2,0,3,1],      #4
        [2,3,0,1]]      #5, 범위 밖
def travel(x, y, d):
    dx, dy = dd[d]
    nx, ny = x+dx, y+dy
    score=0
    while 1:
        if nx<0 or ny<0 or nx>n-1 or ny>n-1:
            nx, ny = nx-dx, ny-dy; score+=1; d=reflex[5][d]
        if a[nx][ny]==-1 or (nx==x and ny == y): return score       #블랙홀 or 제자리
        if 1<= a[nx][ny] <=5:
            score+=1
            d = reflex[a[nx][ny]][d]
        elif 6<= a[nx][ny] <=10:
            for tx, ty in warm[a[nx][ny]]:
                if not(tx==nx and ty==ny):
                    nx, ny = tx, ty
                    break
        dx, dy = dd[d]
        nx, ny = nx+dx, ny+dy

for t in range(int(input())):
    n=int(input())
    a=[list(map(int,input().split()))for _ in range(n)]
    ans=0
    #웜홀 처리만 해줌 될듯, 블랙홀, 반사된느곳은 그때그때 정하고
    warm=[[]for _ in range(11)]
    for i in range(n):
        for j in range(n):
            if 6<= a[i][j] <=10:
                warm[a[i][j]].append((i,j))
    for i in range(n):
        for j in range(n):
            if not a[i][j]:
                for d in range(4):
                    ans = max(ans, travel(i,j,d))
    print('#{} {}'.format(t+1, ans))
