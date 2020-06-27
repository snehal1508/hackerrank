n = int(input())
arr = list(map(int,input().split()))
sortedarr = sorted(arr)
a = []
subarr = []
ctr = 0
for i in range(n):
    if arr[i] != sortedarr[i] :
        ctr += 1
        a.append(i+1)
if ctr == 2:
    print("yes")
    print("swap", a[0],a[1],sep = " ")
else:       
    for i in range(n):
        if arr[i] == sortedarr[i] :
            None
        else:
            subarr.append(arr[i])
    if subarr == sorted(subarr,reverse = True):
        print("yes")
        print("reverse", arr.index(subarr[0])+1,arr.index(subarr[-1])+1,sep=" ")
    else:
        print("no")
