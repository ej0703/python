nums=str(input())

A=nums.split(',')

result=0
while A:
	result += int(A.pop())

print(result)