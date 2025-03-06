L=[]
for i in range(9):
    l=int(input())
    L.append(l)
print(max(L))
print(L.index(max(L))+1)