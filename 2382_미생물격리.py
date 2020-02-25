from collections import*
dd=[(-1,0 ), (1,0), (0,-1), (0,1)]  #UDLR
def checkD(d):
    if d==0: return 1
    if d==1: return 0
    if d==2: return 3
    return 2
for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=[]
    for i in range(k):
        x, y, v, d = map(int,input().split())       #x, y, 값, 방향
        d-=1
        a.append((x, y, v, d))
    for i in range(m):                              #m시간 동안
        check=[[0]*n for _ in range(n)]
        add_list = []
        for x, y, v, d in a:
            dx, dy = dd[d]                          #다음 방향
            nx, ny = x+dx, y+dy
            if nx<1 or ny<1 or nx>=n-1 or ny>=n-1:  #테두리 닿으면
                d = checkD(d)                       #방향 반대로
                check[nx][ny] = (v//2, v//2, d)     #check [합][최대값][방향], 반으로 잘라서 줌
                add_list.append((nx, ny))           #다음 값 추가용
            elif check[nx][ny]:                     #이미 방문한 곳이면
                SUM, MAX, nd = check[nx][ny]
                if check[nx][ny][1] < v:            #값 비교해야함
                    MAX = v; nd = d                 #v가 크면 최대값, 방향 바꿔줌
                check[nx][ny] = (SUM+v, MAX, nd)    #합, 최대값, 방향 check에 최신화
            elif not check[nx][ny]:                 #방문하지 않은 곳이면
                check[nx][ny] = (v, v, d)           #값, 방향 그대로
                add_list.append((nx, ny))           #다음 값 추가용
        a=[]
        for x, y in add_list:                       #다음 값들 추가
            a.append((x, y, check[x][y][0], check[x][y][-1]))       #여기 3번째 값 [nx][ny][0]으로 해서 안나왔었음
    res=0
    for x, y, v, d in a:
        res += v
    print('#{} {}'.format(t+1, res))
