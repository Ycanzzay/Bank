N = int(input())
k = int(input())
l = list(range(1,N + 1))
while len(l) !=1:
    index = k%len(l)
    k = index; del l[k]; k+=2
    print(l)