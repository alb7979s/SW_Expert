def solve(pos, res):
    ans=INF
    if pos >= 12: return res
    ans = min(ans, solve(pos+1, res+(a[pos])*b[0]), #여기 b[0] 안곱해줬었음
              solve(pos+1, res+b[1]),
              solve(pos+3, res+b[2]),
              solve(pos+12, res+b[3]))
    return ans

INF=1e9
for t in range(int(input())):
    b = list(map(int,input().split()))
    a = list(map(int,input().split()))
    print('#{} {}'.format(t+1, solve(0,0)))
