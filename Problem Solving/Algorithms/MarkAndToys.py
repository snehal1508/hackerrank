nk = input().split()
n = int(nk[0])
k = int(nk[1])
prices = list(map(int, input().rstrip().split()))
total = cnt =0
for i in sorted(prices):
    total += i
    if total<=k:
        cnt += 1
    else:
        break
print(cnt)
