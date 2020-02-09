def solve():
    dup=[]
    temp=[]
    for i in range(len(a)): temp.append(a[i])
    for _ in range(n//4):
        for i in range(n):
            temp[i] = a[(i+(n-1))%n]
        t=0
        while 1:
            if t+(n//4) > n: break
            string=''
            for j in range(n//4):
                string += temp[t+j]
            cal = int(string, 16)
            if cal not in dup:
                dup.append(cal)
            t+=(n//4)
        for i in range(len(a)): a[i] = temp[i]      #여기서 변수 __이거 썼다가 아....

    dup.sort(reverse=True)
    try:return dup[k-1]
    except:print(dup)
for t in range(int(input())):
    n, k =map(int,input().split())
    a=list(input())
    print('#{} {}'.format(t+1, solve()))
