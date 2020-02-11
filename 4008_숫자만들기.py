from collections import*
def solve(pos, res):
    global MAX, MIN
    if pos == n:
        MAX=max(MAX, res)
        MIN=min(MIN, res)
        return
    if a[0]!=0:
        a[0]-=1
        solve(pos+1, res+num[pos])
        a[0]+=1
    if a[1]!=0:
        a[1]-=1
        solve(pos+1, res-num[pos])
        a[1]+=1
    if a[2]!=0:
        a[2]-=1
        solve(pos+1, res*num[pos])
        a[2]+=1
    if a[3]!=0:
        a[3]-=1
        solve(pos+1, int(res/num[pos]))
        a[3]+=1
    return

INF=1e9
for t in range(int(input())):
    MAX=-INF; MIN=INF
    n=int(input())
    a=list(map(int,input().split()))
    num=list(map(int,input().split()))
    solve(1, num[0])
    print('#{} {}'.format(t+1, MAX-MIN))
