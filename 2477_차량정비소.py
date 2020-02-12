#다시 차분히 살펴보기
from collections import*
for t in range(int(input())):
    n, m, K, A, B = map(int,input().split())
    A-=1;B-=1
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    T = list(map(int,input().split()))
    k=1                 #k고객, wait접수, fix수리
    wait_list=[0]*n
    fix_list=[0]*n
    res=0
    q=deque()           #수리 대기
    q1=deque()
    temp=deque(); temp2=[]
    for i in range(k):
        temp2.append([T[i], i+1])    #시간, 고객번호
    temp2.sort()
    for x,y in temp2:
        temp.append([x,y])
    wt=0
    while 1:
        f1, f2 = 0, 0
        while temp:
            if temp[0][0]==wt:
                time, cusNum = temp.popleft()
                q1.append([time, cusNum])
            else:break
        for i in range(n):  #접수 대기에 넣음
            if not wait_list[i]:
                if q1:
                    time, cusNum = q1.popleft()
                    wait_list[i] = [a[i], i, cusNum]
                    f1=1
        for i in range(n):  #접수진행
            if not wait_list[i]:continue
            if wait_list[i][0]-1 ==0:   #접수 완료 했으면 수리 대기로
                time, waitNum, cusNum = wait_list[i]
                q.append((waitNum, cusNum))
                wait_list[i]=0
            else:
                wait_list[i][0]-=1
                f1=1
        for i in range(m):
            if not fix_list[i]:     #없는 경우
                if q:
                    waitNum, cusNum = q.popleft()
                    fix_list[i]=[b[i], i, waitNum, cusNum]  #시간, 수리번호, 접수번호, 고객
                    f2=1
        for i in range(m):  #수리진행
            if not fix_list[i]:continue     #수리할게 없으면 넘겨
            if fix_list[i][0]-1 == 0:
                time, fixNum, waitNum, cusNum = fix_list[i]
                fix_list[i]=0
                if fixNum == B and waitNum == A: res += cusNum
            else:
                fix_list[i][0]-=1
                f2=1
        if k > K and not f1 and not f2: break
        wt+=1
    print("#{} {}".format(t+1, res))

