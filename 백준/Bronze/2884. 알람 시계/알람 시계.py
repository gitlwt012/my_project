H,M=map(int,input().split())
if M-45<0:
    if H==0:
        H=23
    else:
        H=H-1
    M=M+15
    print(H,M)
else:
    M=M-45
    print(H,M)