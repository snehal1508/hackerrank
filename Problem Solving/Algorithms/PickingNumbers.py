n = int(input().strip())

a = list(map(int, input().rstrip().split()))
freq = [0 for i in range(101)]
max_pair = 0
for n in a:
    freq[n] += 1
    max_pair = max(max_pair, max((freq[n] + freq[n-1]), (freq[n] + freq[n+1])))
print(max_pair)
