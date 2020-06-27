t = int(input())

for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    temp = k
    if(k == 0):
        for i in range(1, n+1):
            print(i, end = " ")
    elif((n % (2*k)) == 0):
        for i in range(1, n+1):
            print(i+temp, end = " ")
            if(i % k == 0):
                temp = temp * -1                       
    else:
        print(-1, end = " ")
        
    print()
