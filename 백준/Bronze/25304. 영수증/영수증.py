X=int(input())
N=int(input())
x=0
for i in range(N):
    a,b=map(int,input().split())
    x+=a*b
if X==x:
    print('Yes')
else:
    print('No')