from math import *


def teta(z):
	if z < 0:
		return 0
	return 1

def p_k(k, x_1, y_1, x_2, y_2):
	ans = 0
	for i in range(k):
		ans += (sqrt((x_1[i] - x_2[i])**2 + (y_1[i] - y_2[i])**2))**2
	return sqrt(ans)

def c_k_l(k, l):
	summ = 0
	for n1 in range(N-k):
		for n2 in range(N-k):
			summ += teta(l - p_k(k, x[n1:n1+k], y[n1:n1+k], x[n2:n2+k], y[n2:n2+k]))
	return summ / (N**2)

t = 100
N = 1000
a, b = 1, 1
k = 40

x = [a * cos(i/t) for i in range(N  + 1)]
y = [b * sin(i/t) for i in range(N  + 1)]

l = 0.5

dc = log(c_k_l(1,l))/log(l)
for i in range(2, k):
	print(dc)
	dc_new = log(c_k_l(i,l))/log(l)
	if abs(dc - dc_new) < 0.05:
		print("END: k = ", i)
		break
	dc = dc_new	
