from collections import*
U, R, D, L = 1, 2, 4, 8
dd = [(-1,0), (0,1), (1,0), (0,-1)]
IN = [[0],          #입구
      [U|R|D|L],    #1
      [U|D],        #2
      [L|R],        #3
      [D|L],        #4
      [L|U],        #5
      [R|U],        #6
      [R|D]]        #7
OUT = [[0],         #출구
       [U|R|D|L],
       [U|D],
       [L|R],
       [U|R],
       [R|D],
       [L|D],
       [U|L]]
for t in range(int(input())):
    n, m, r, c, l = map(int,input().split())
    a = [list(map(int,input().split()))for _ in range(n)]
    check = [[0]*m for _ in range(n)]
    q=deque()
    for i in range(4):      #초기값 셋팅
        if OUT[a[r][c]][0] & (1<<i):           #&으로 교집합 해야는디 |로 합집합 해버림
            q.append((r, c, i, 1))             #초기 시간1로 해야 했음
    check[r][c]=1
    while q:
        x, y, d, c = q.popleft()
        if c>=l: continue        #break도 됨
        dx, dy = dd[d]
        nx, ny = x+dx, y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>m-1 or check[nx][ny]: continue
        if IN[a[nx][ny]][0] & (1<<d):
            check[nx][ny]=1
            for j in range(4):
                if OUT[a[nx][ny]][0] & (1<<j):
                    q.append((nx, ny, j, c+1))
    res = 0
    for i in range(n):
        res += sum(check[i])
    print('#{} {}'.format(t+1, res))
