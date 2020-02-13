from collections import*
for t in range(int(input())):
    n, m, K, A, B = map(int,input().split())    #접수창고 개수, 수리창고 개수, 고객 수, 찾을 접수번호, 찾을 수리번호
    A-=1;B-=1
    a=list(map(int,input().split()))    #접수 걸리는 시간들
    b=list(map(int,input().split()))    #수리 걸리는 시간들
    T = list(map(int,input().split()))  #고객 도착 시간, 온 순서대로
    k=1                 #k고객, wait접수, fix수리
    wait_list=[0]*n
    fix_list=[0]*n
    res=0
    q=deque()           #수리 대기
    kq=deque()          #고객 queue
    for i in range(K):
        kq.append((T[i], i+1))      #고객 도착시간, 고객 번호
    wt=0        #전체 시간
    q1=deque()
    end=max(T)
    while 1:
        f1, f2 = 0, 0
        while kq:
            if kq and kq[0][0] == wt:
                _, k = kq.popleft()
                q1.append(k)    #접수 대기
            else:break
        for i in range(n):  #접수에 넣음
            if not wait_list[i]:    #접수하는곳 비었으면
                if q1:
                    cusNum = q1.popleft()
                    wait_list[i] = [a[i], i, cusNum]    #접수시간, 접수번호, 고객
                    f1=1
        for i in range(n):  #끝낸 접수 처리
            if not wait_list[i]:continue    #비어 있으면 넘김
            if wait_list[i][0]-1 ==0:       #접수 완료 했으면 수리 대기로
                time, waitNum, cusNum = wait_list[i]
                q.append((waitNum, cusNum))
                wait_list[i]=0
                if q1:
                    cusNum = q1.popleft()
                    wait_list[i] = [a[i], i, cusNum]    #접수시간, 접수번호, 고객
                    f1=1
            else:
                wait_list[i][0]-=1
                f1=1
        for i in range(m):
            if not fix_list[i]:     #수리 하는곳 빈 경우
                if q:
                    waitNum, cusNum = q.popleft()
                    fix_list[i]=[b[i], i, waitNum, cusNum]  #시간, 수리번호, 접수번호, 고객
                    f2=1
        for i in range(m):  #끝낸 수리 처리
            if not fix_list[i]:continue     #수리할게 없으면 넘겨
            if fix_list[i][0]-1 == 0:
                time, fixNum, waitNum, cusNum = fix_list[i]
                fix_list[i]=0
                if fixNum == B and waitNum == A: res += cusNum  #지갑 속 찾을 번호들 같으면 결과값에 고객번호 더함
                if q:
                    waitNum, cusNum = q.popleft()
                    fix_list[i]=[b[i], i, waitNum, cusNum]  #시간, 수리번호, 접수번호, 고객
                    f2=1
            else:
                fix_list[i][0]-=1
                f2=1
        if wt>end and not f1 and not f2: break
        wt+=1
    print("#{} {}".format(t+1, res if res != 0 else -1))

