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
            heappush(pq,[a[i][j], i, j, 1]) #마지막 1이면 활성 예정
    for _ in range(k):
        dic={};temp=[]
        for i in range(len(pq)):
            if pq[i][0]-1 == 0:
                pq[i][0]-=1
                v, x, y, h = heappop(pq)
                temp.append((x, y))
                if h==0: continue
                for dx, dy in dd:
                    nx, ny = x+dx, y+dy
                    if nx<0 or ny<0 or nx>n-1 or ny>m-1 or check[nx][ny]==1: continue
                    if check[nx][ny]==0:    #0안옴, 1활성or완료, 2대기
                        check[nx][ny]=2
                        dic[(nx,ny)]=a[nx][ny]
                    elif check[nx][ny]==2:
                        if dic.get((nx,ny)) < a[nx][ny]:
                            dic[(nx,ny)] = a[nx][ny]
            else:
                for j in range(len(pq)):
                    pq[j][0]-=1
                break

        for key, v in dic.items():
            nx, ny = key
            check[nx][ny]=1
            heappush(pq,[v, nx, ny, 1])
        for x, y in temp:
            heappush(pq,(a[x][y], x, y, 0))
    print("#{} {}".format(t+1, len(pq)))

