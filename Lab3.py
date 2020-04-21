def EA(a, N): #Euclidean Algorithm
	if a == 0:
		return N
	return EA(N % a, a)

def inverse(a, N): #Finds inverse modulo
	a = a % N
	for x in range(1, N):
		if ((a * x) % N == 1):
			return x
	else:
		print('None')

def EEA(N, a, x, y): #Extended Euclidean Algorithm
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

print('Euclidian Algorithm, Input the numbers below:')
a = input()
N = input()
print('GCD of',a,'and',N,'is',EA(int(a), int(N)))
print('The modulo inverse of',N,'and',a,'is',inverse(int(N), int(a)))

print('Extended Euclidian Algorithm:')
x = -1
y = 17
N = 84
a = 5
print(x,'*',N,'+',y,'*',a)
print(N,'mod',a,'is',EEA(N, a, x, y))
