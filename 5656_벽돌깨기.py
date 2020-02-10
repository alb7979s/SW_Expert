from collections import*
def fire(x, y, c):
    q=deque()
    q.append((x, y, a[x][y]))
    a[x][y] = 0
    while q:
        x, y, t = q.popleft()
        for dx, dy in dd:
            nx, ny = x, y
            for i in range(t - 1):
                nx, ny = nx+dx, ny+dy
                if nx<0 or ny<0 or nx>n-1 or ny>m-1 or not a[nx][ny]: continue
                c+=1
                if a[nx][ny] > 1:
                    q.append((nx, ny, a[nx][ny]))
                a[nx][ny]=0

    return c
arr=[]
def arrange():
    for i in range(m):
        q=[]
        for j in range(n):
            if a[j][i]:
                q.append(a[j][i])
            a[j][i]=0
        while q:
            a[j][i] = q.pop()
            j-=1

def solve(cnt, ans):
    res=0
    global a
    arrange()
    if cnt == k or temp == ans: return ans #끝에 다다르거나 다 터친 경우
    for i in range(m):
        for j in range(n):
            if a[j][i]:
                b=[x[:] for x in a]
                res = max(res, solve(cnt+1, ans + fire(j, i, 1)))
                a=[x[:] for x in b]
                break
    return res
dd=[(-1,0),(0,1),(1,0),(0,-1)]
for t in range(int(input())):
    k, m, n = map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    temp=0
    for i in range(n):
        for j in range(m):
            if a[i][j]:temp+=1
    print("#{} {}".format(t+1, temp-solve(0, 0)))
