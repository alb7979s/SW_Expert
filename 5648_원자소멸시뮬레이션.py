from collections import*        #시간초과 떴다 통과 됐다 아주 지 맘대로임..
dd=[(0.5, 0), (-0.5, 0), (0, -0.5), (0, 0.5)]   #상하좌우
for t in range(int(input())):
    n=int(input())
    q=deque()
    for i in range(n):
        y, x, d, e = map(int,input().split())
        q.append((x,y,d,e))
    dic={}; res=0
    while 1:
        if not q or len(q)<2: break
        temp=[]
        for i in range(len(q)):
            x, y, d, e = q.popleft()
            dx, dy = dd[d]
            nx, ny = x+dx, y+dy
            if nx<-1000 or ny<-1000 or nx>1000 or ny>1000: continue
            try:
                if dic[(nx, ny)]:
                    dic[(nx, ny)]=0
                res += e
                continue
            except:
                dic[(nx, ny)]=e
                temp.append((nx, ny, d, e))
        for x, y, d, e in temp:
            try:
                if not dic[(x, y)]: #충돌된거
                    res += e
                else:
                    q.append((x, y, d, e))
            except:
                q.append((x, y, d, e))
            del dic[(x, y)]
    print('#{} {}'.format(t+1, res))

