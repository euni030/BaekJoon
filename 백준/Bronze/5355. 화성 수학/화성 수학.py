T=int(input())

for i in range(T):
    case=list(map(str,input().split()))
    result=float(case[0])
    for j in range(len(case)):
        if case[j]=='@':
            result*=3
        elif case[j]=='%':
            result+=5
        elif case[j]=='#':
            result-=7
    print("%0.2f"%result)