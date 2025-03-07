N=int(input())
L=input()
M=','.join(L)
S=0
for i in range(0,2*N,2):
    S+=int(M[i])
print(S)