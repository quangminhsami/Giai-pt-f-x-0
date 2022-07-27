import math

print("Nhập khoảng cách ly nghiệm a và b:")
print("Nhập a = ")
a = float(input())
print("Nhập b = ")
b = float(input())
print("Nhập sai số epxilon = ")
epxilon = float(input())

if math.sin(a) > 0:
	sig = 1
else:
	sig = -1

i = 0

c = (a + b) / 2

while b - a >= epxilon:
	z = math.sin(c)
	if z == 0:
		print("Số e gần đúng là" + " " + str(c))
	else:
		if z * sig > 0:
			a = (a + b) / 2
		else:
			b = (a + b) / 2
	c = (a + b) / 2
	i += 1
	print("Số e gần đúng là" + " " + str(c))
print("số lần lặp : " + str(i))


 
