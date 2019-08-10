import secrets
n = secrets.randbelow(10000)
if n < 10:
	print('Random PIN is 000' + str(n))
elif n < 100:
	print('Random PIN is 00' + str(n))
elif n < 1000:
	print('Random PIN is 0' + str(n))
else:
	print('Random PIN is ' + str(n))
