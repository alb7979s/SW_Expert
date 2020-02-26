def cal(pos, res, MAX, f):
    ans=0
    if MAX > c: return 0
    if pos == m :
        return res
    if f==0:ans = max(ans, cal(pos+1, res, MAX, 0), cal(pos+1, res+one[pos]**2, MAX+one[pos], 0))
    if f==1:ans = max(ans, cal(pos+1, res, MAX, 1), cal(pos+1, res+two[pos]**2, MAX+two[pos], 1))
    return ans
def solve(ix, iy, jx, jy):
    for i in range(m):
        one.append(a[ix][iy+i])
        two.append(a[jx][jy+i])
    return cal(0,0,0,0) + cal(0,0,0,1)

for t in range(int(input())):
    n, m, c =map(int,input().split())
    a = [list(map(int,input().split()))for _ in range(n)]
    res = 0
    for ix in range(n):
        for iy in range(n):
            if iy + m > n: break
            for jx in range(ix, n):
                for jy in range(n):
                    if jy + m > n : break         # or iy>=jy로 했는데 tc 추가하면 오류날듯 아래 수정
                    if iy+m > jy: continue        # continue로 수정
                    one=[]; two=[]
                    res = max(res, solve(ix, iy, jx, jy))
    print('#{} {}'.format(t+1, res))
