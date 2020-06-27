for _ in range(int(input())):
    n,k = map(int,input().split())
    a = map(int,input().split())
    print("YES" if len([0 for i in a if i<1])<k else "NO")
