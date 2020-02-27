'''
f=open('foo.txt','w')
try:
	f.write()

except FileNotFoundError as e:
	print(e)

finally: f.close()

try:
	a=[1,2]
	print(a[3])
	4/0
except ZeroDivisionError:
	print("0으로 나눌 수 없습니다.")
except IndexError:
	print("인덱싱 할 수 없습니다.")
'''
class Bird:
	def fly(self):
		raise NotImplementedError

class Eagle(Bird):
	def fly(self):
		print("very fast")
eagle=Eagle()
eagle.fly()