def fev(n):
	if n==0:
		return 1
	elif n==1:
		return 1
	else:
		return fev(n-1)+fev(n-2)

a=int(input())
n=0

while fev(n)<=a:
	print(fev(n))
	n += 1