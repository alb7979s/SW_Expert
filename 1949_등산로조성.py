#1949. 등산로 조성
# n*n 지도
# 최대한 긴 등산로
#1. 가장 높은 봉우리에서 시작
#2. 등산로 올라갈수록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로로 연결
#3. 딱 한 곳을 정해서 최대 K깊이만큼 지형 깎을 수 있음

#bfs로 풀고픈데 왔던곳 다시 방문 안하게 d 조절하면 될듯?
from collections import*
def searchD(d):
    if d==0: return 2
    if d==1: return 3
    if d==2: return 0
    return 1
def bfs():
    q=deque()
    ans=0
    for x, y in maru:
        q.append((x, y, 1, -1))
    while q:
        x, y, c, d = q.popleft()
        for i in range(4):
            if d == searchD(i): continue        #전에꺼랑 반대방향이면 넘어감
            dx, dy = dd[i]
            nx, ny = x+dx, y+dy
            if nx<0 or ny<0 or nx>n-1 or ny>n-1 or a[nx][ny]>=a[x][y]:
                ans = max(ans, c)
                continue
            q.append((nx, ny, c+1, i))
    return ans

dd=[(-1,0),(0,1),(1,0),(0,-1)]  #URDL
for t in range(int(input())):
    n, k = map(int,input().split())
    a=[]
    MAX=0
    for i in range(n):
        a.append(list(map(int,input().split())))
        MAX = max(MAX, max(a[i]))
    maru=[]
    for i in range(n):
        for j in range(n):
            if a[i][j] == MAX: maru.append((i,j))
    max_len=0
    for i in range(n):
        for j in range(n):
            for l in range(k):
                a[i][j]-=1
                max_len = max(max_len, bfs())
            a[i][j]+=k
    print('#{} {}'.format(t+1, max_len))
