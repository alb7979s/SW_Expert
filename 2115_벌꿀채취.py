def solve(arr, pos, cost, ans):
    res=0
    if pos == len(arr):
        print(len(arr))
        return ans
    if cost + arr[pos] <= C:
        res = max(res, solve(arr, pos+1, cost+arr[pos], ans+arr[pos]**2))
    res = max(res, solve(arr, pos+1, cost, ans))
    return res

for t in range(int(input())):
    n,m,C = map(int,input().split())
    a=[list(map(int,input().split()))for _ in range(n)]
    res=0
    for ix in range(n):
        for iy in range(n):
            if iy+m > n-1: continue
            for jx in range(n):
                for jy in range(n):
                    if jy+m > n-1: continue
                    b=[];c=[]
                    if ix == jx and iy+m >= jy: continue
                    for i in range(m):
                        b.append((a[ix][iy+i]))
                        c.append((a[jx][jy+i]))
                res = max(res, solve(b,0,0,0) + solve(c,0,0,0))
    print('#{} {}'.format(t+1, res))