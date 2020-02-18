from collections import*
def solve(pos, cnt):
    res=INF
    if pos == len(man):
        if cnt == len(man):
            temp1 = [x for x in wait1]
            temp2 = [x for x in wait2]
            return cal(temp1, temp2)
    for i in range(len(stairs)):
        dx, dy = stairs[i]
        x, y = man[pos]
        if i==0:
            wait1.append(abs(x-dx)+abs(y-dy))
            res = min(res, solve(pos+1, cnt+1))
            wait1.pop()
        else:
            wait2.append(abs(x-dx)+abs(y-dy))
            res = min(res, solve(pos+1, cnt+1))
            wait2.pop()
    return res
def cal(wait1, wait2):
    global T
    q1, q2 = deque(), deque()
    wait1.sort(reverse=True)
    wait2.sort(reverse=True)
    T=0
    while 1:
        if not(wait1 or wait2 or q1 or q2): break
        wait1, q1 = waiting_processing(wait1, q1, 1)
        wait2, q2 = waiting_processing(wait2, q2, 2)
        T+=1
    return T+1

INF=1e9
def waiting_processing(wait, q, f):
    while 1:
        if wait and T >= wait[-1] and len(q) < 3:
            wait.pop()
            if f==1:
                q.append(a[stairs[0][0]][stairs[0][1]])
            elif f==2:
                q.append(a[stairs[1][0]][stairs[1][1]])
        else:break
    q = q_processing(q)
    return (wait, q)

def q_processing(q):
    temp=0
    for i in range(len(q)):
        if q[i]-1 <= 0:
            temp+=1
        else: break
    for j in range(temp): q.popleft()
    for i in range(len(q)):
        q[i]-=1
    return q

for t in range(int(input())):
    n = int(input())
    man=[]; stairs=[]
    a = [list(map(int,input().split()))for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1: man.append((i,j))
            elif a[i][j]: stairs.append((i,j))
    wait1=[]
    wait2=[]
    T=0
    print("#{} {}".format(t+1, solve(0, 0)))
