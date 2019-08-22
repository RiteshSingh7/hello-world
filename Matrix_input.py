# Count Sorted Rows (GfG)

def test(arr, dec = False):
    i = 1
    while i < len(row):
        if dec:
            if row[i] >= row[i-1]:
                break
        else:
            if row[i] <= row[i-1]:
                break
        i += 1
    if i == len(row):
        return True
    else:
        return False

t = int(input())
result = []
for _ in range(t):
    m,n = map(int, input().split())
    arr = list(map(int, input().split()))[:m*n]
    matrix = [[arr[j + i*n] for j in range(n)] for i in range(m)]
    
    ans = 0
    for row in matrix:
        if test(row):
            ans += 1
        elif test(row, dec=True):
            ans += 1
    result.append(ans)

for ans in result:
    print(ans)

# See how to form matrix using single line input
    