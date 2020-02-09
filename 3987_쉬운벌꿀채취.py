def solve(arr, pos, cost, ans):
    res=0
    if pos == len(arr):
        return ans
    if cost + arr[pos] <= C:
        res = max(res, solve(arr, pos+1, cost+arr[pos], ans+arr[pos]**2))
    res = max(res, solve(arr, pos+1, cost, ans))
    return res

for t in range(int(input())):
    n, C = map(int,input().split())
    a=list(map(int,input().split()))
    print('#{} {}'.format(t+1, solve(a, 0, 0, 0)))