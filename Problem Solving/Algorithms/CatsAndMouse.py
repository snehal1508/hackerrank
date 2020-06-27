q = int(input())
for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])

    a = abs(x-z)
    b = abs(y-z)    

    print("Cat A" if a<b else "Cat B" if b<a else "Mouse C")
