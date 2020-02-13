from heapq import*

MAX=650
dd=[(-1,0),(0,1),(0,-1),(1,0)]
for t in range(int(input())):
    check = [[0] * 651 for _ in range(651)]
    n,m,k=map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    sx=MAX//2 - n//2; sy=MAX//2 - m//2
    pq=[]
    for i in range(n):          #초기값 배열에
        for j in range(m):
            if a[i][j]:
                check[sx+i][sy+j]=1
                heappush(pq,[a[i][j], a[i][j], sx+i, sy+j, 1]) #마지막 1이면 활성 예정
    for _ in range(k):
        dic={};temp=[]
        for i in range(len(pq)):
            time, v, x, y, h = heappop(pq)
            if time > 0:
                heappush(pq,[time, v, x, y, h])
                for j in range(len(pq)):    #시간 남는애들 시간 -1해줌
                    pq[j][0]-=1
                break
            if h == 0:      #죽는 세포면
                check[x][y]=1
                continue
            temp.append((v, x, y)) #활성화 된거 나중에 마지막0으로 해서 추가해줘야함
            for dx, dy in dd:   #네방향 번식
                nx, ny = x+dx, y+dy
                if nx<0 or ny<0 or nx>650 or ny>650 or check[nx][ny]==1: continue
                if check[nx][ny]==0:    #0안옴, 1활성or완료, 2대기
                    check[nx][ny]=2
                    dic[(nx,ny)] = v
                elif check[nx][ny]==2:
                    if dic.get((nx,ny)) < v:
                        dic[(nx,ny)] = v
        for key, v in dic.items():
            nx, ny = key
            check[nx][ny]=1
            heappush(pq,[v, v, nx, ny, 1])
        for v, x, y in temp:
            heappush(pq,[v, v, x, y, 0])
        res=len(pq)
        for i in range(len(pq)):
            if pq[i][0] == 0 and pq[i][-1] == 0:
                res-=1
        print(res)
    print("#{} {}".format(t+1, res))
