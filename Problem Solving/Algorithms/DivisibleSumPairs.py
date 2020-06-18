
n,k = [int(x) for x in input().strip().split(' ')]
ar = [int(a_temp) for a_temp in input().strip().split(' ')]
cnt = 0
for i in range(n-1):
    for j in range (i+1, n):
        if (ar[i]+ar[j])%k == 0:
            cnt+=1

print(cnt)
