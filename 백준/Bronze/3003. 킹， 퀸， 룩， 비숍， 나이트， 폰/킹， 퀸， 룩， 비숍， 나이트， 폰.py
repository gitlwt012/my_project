L=list(map(int,input().split()))
l=[1,1,2,2,2,8]
l_L=[l[i]-L[i] for i in range(len(L))]
for i in range(len(l_L)):
    print(l_L[i],end=' ')