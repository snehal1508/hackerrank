def countSort(arr,n):
    coll = dict()      
    count = 0          
    for [i,j] in arr:
        if count < n/2:
            coll.setdefault(int(i),[]).append('-')
            count += 1
        else:
            coll.setdefault(int(i),[]).append(j)   
    ans = []
    ele = list(sorted(list(coll.keys())))   
    for i in ele:
        temp = coll[i]
        ans.extend(temp)
    print(' '.join(ans))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr,n)
