inStr =input("문자를 입력하세요: ")
'''
inStr_list=list(inStr)
inStr_list.reverse()

print("거꾸로 출력 --> ",''.join(inStr_list))
'''
outStr=""
count=len(inStr)

for i in range(count):
	outStr += inStr[count-(i+1)]

print("거꾸로 출력 --> %s"%outStr)