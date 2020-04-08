def EA(a, N):
	if a == 0:
		return N
	return EA(N % a, a)

def EEA(N, a, x, y):
	if N == 0:
		x = 0
		y = 1
		return a

	x1 = 1
	y1 = 1  # To store results of recursive call
	EA = EEA(a % N, N, x1, y1)

	x = y1 - (a / N) * x1
	y = x1

	return EA

print('Euclidian Algorithm:')
a = 975
N = 1000
print('GCD of',a,'and',N,'is',EA(N, a))

print('Extended Euclidian Algorithm:')
x = -1
y = 17
N = 84
a = 5
print(x,'*',N,'+',y,'*',a)
print(N,'mod',a,'is',EEA(N, a, x, y))