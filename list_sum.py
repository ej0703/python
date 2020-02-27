A=[20,55,67,82,45,33,90,87,100,25]

result=0
while A:
	a=A.pop()
	if a>=50:
		result+=a

print(result)