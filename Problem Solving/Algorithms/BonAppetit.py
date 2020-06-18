nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())
sum=0
for i in range(n):
    if i == k :
        continue
    else:
        sum += bill[i]

if(b == sum/2):
    print("Bon Appetit")
else:
    print(int(b-sum/2))


