# Aggressive Cows (SPOJ)

def test(dis, cows, barn):
	i = flag = 0
	while cows > 0 and i < len(barn):
		if barn[i] >= flag:
			cows -= 1
			flag = barn[i] + dis
		i += 1
	return True if cows == 0 else False

t = int(input())
result = []
for _ in range(t):
	n,c = map(int, input().split())
	barn = []
	for ite in range(n):
		barn.append(int(input()))

	barn.sort()
	low,high = 1, 10**9
	while low <= high:
		dis = low + (high-low)//2
		if test(dis, c, barn):
			low = dis + 1
		else:
			high = dis - 1
	result.append(high)

for ans in result:
	print(ans)
