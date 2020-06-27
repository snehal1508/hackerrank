n,k = map(int,input().strip().split(' '))
prbs = [int(p) for p in input().strip().split(' ')]
mp = 0
pc = 1

for p in prbs:
    s = 1
    while True:
        fp, lp = s, min(s+k-1,p)
        if fp <= pc <= lp:
            mp += 1
        pc += 1
        if (s+k > p):
            break
        else:
            s += k
print(mp)
