from math import pow

def kaprekarNumbers(p, q):
    result = []
    for i in range(p, q + 1):
        x = str(int(pow(i, 2)))
        l = x[0:int(len(x) / 2)] if x[0:int(len(x) / 2)] else 0
        r = x[int(len(x) / 2):len(x)] if x[int(len(x) / 2):len(x)] else 0
        if(int(l) + int(r) == i): result.append(str(i))
    print(' '.join(result) if len(result) > 0 else 'INVALID RANGE')

if __name__ == '__main__':
    kaprekarNumbers(int(input()), int(input()))
