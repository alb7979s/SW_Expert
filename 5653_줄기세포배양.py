#dictionary 사용법 찾아가지고 마무리 짓기
from heapq import*

MAX=650
dd=[(-1,0),(0,1),(0,-1),(1,0)]
for t in range(int(input())):
    check = [[-1] * 650 for _ in range(650)]
    n,m,k=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    sx=MAX//2 - n//2; sy=MAX//2 - m//2
    pq=[]
    for i in range(n):
        for j in range(m):
            check[sx+i][sy+j]=1
            heappush(pq,[a[i][j], i, j])
    for _ in range(k):
        dic={}
        for i in range(len(pq)):
            pq[i][0]-=1
            if pq[i][0] == 0:
                v, x, y = heappop(pq)
                for dx, dy in dd:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>m-1 or check[nx][ny]==1: continue
                    if check[nx][ny]==0:    #0안옴, 1활성or완료, 2대기
                        check[nx][ny]=2
                        #사전에 추가
                    elif check[nx][ny]==2:
                        #사전에 추가된거 바꿔 dic=(nx,ny):a[nx][ny]
        for j in range(len(dic)):#사전 전부
            #heappush(pq,[(,,)]) 사전에서 a[nx][ny], nx, ny꺼내 저장
    print("#{} {}".format(t+1, len(pq)))


