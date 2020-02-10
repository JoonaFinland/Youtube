# Fizz Buzz

for x in range(1000000):
	if x % 3 == 0:
		print('FIZZ',end='')
	if x % 5 == 0:
		print('BUZZ',end='')
	if x % 3 != 0 and x % 5 != 0:
		print(x, end='')
	print()