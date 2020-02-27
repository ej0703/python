import operator
import sqlite3

foods=["떡볶이","짜장면","라면","피자","맥주","치킨","삼겹살"]
sides=["오뎅","단무지","김치","피클","새우깡","무우","소주"]

for i,j in zip(foods,sides):
	print(i,'-->',j)