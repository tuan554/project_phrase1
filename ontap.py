# i = 1
# t = 0
# while i < 101:
# 	if i%2==0:
# 		t = t + i
# 	i = i + 1
# print(t)

# a = 5
# if a % 3 == 0 and a % 5 == 0:
# 	print("c")
# elif a % 3 == 0:
# 	print("a")
# elif a % 5 == 0:
# 	print("b")

# def day(n):
# 	t = 0
# 	i = 1
# 	while i <= n:
# 		q = 1
# 		w = 1
# 		while w <= i:
# 			q = q*w
# 			w = w+1
# 		t = t + q
# 		i = i + 1
# 	return t
# print(day(1))

# Bai tap gui qua gmail
# Bai 6
# a = 1
# while a < 100:
# 	b = 1
# 	while b <= a:
# 		if a / b == b:
# 			print(a)
# 			b = b + 1
# 		else:
# 			b = b + 1
# 	a = a + 1

#Bai  8
# a = 21
# if a < 10:
# 	print (a)
# elif a < 100:
# 	a = int(a / 10) + ((a-int(a/10)*10)*10)
# 	print(a)
# elif a < 1000:
# 	a = int(a / 100) + ((int(a/10)-int(int(a/10)/10)*10)*10) + ((a - ((int(a/10)-int(int(a/10)/10)*10)*10) - (int(a / 100)*100))*100)
# 	print(a)

# Bai 4
# def day(n):
# 	t = 0
# 	i = 1
# 	while i <= n:
# 		q = 1
# 		w = 1
		
# 		while w <= i:
# 			q = q*w
# 			w = w+2

# 		t = t + q
# 		i = i + 2
# 	return t
# print(day(4))

#Bai 7
# b = 169
# a = b
# if a < 10:
# 	print (a)
# elif a < 100:
# 	a = int(a / 10)*10
# 	print(a)
# 	a = b
# 	a = a-int(a/10)*10
# 	print(a)
# elif a < 1000:
# 	a = int(a / 100)*100
# 	print(a)
# 	a = b
# 	a = a - ((int(a/10)-int(int(a/10)/10)*10)*10) - (int(a / 100)*100)
# 	print(a)
# 	a = b
# 	a = ((int(a/10)-int(int(a/10)/10)*10)*10)
# 	print(a)

# def reverse(str):
# 	i = len(str)
# 	sum = ""
# 	while i > 0:
# 		sum = sum + str[i - 1]
# 		i = i - 1
# 	return sum

# print(reverse(str(11122)))
# def tccs(i):
# 	i = str(i)
# 	c = 0
# 	sum = 0
# 	while c < len(i):
# 		sum = sum + int(i[c])
# 		c = c + 1
# 	return sum
# print(tccs(2231))



# b = "on on"
# a = int(len(b)/2)
# c = b[0:a]
# d = b[a+1:]
# if c == d:
# 	print ("True")
# else:
# 	print("False")


#1)In ra cac so nguyen to tu 1 den 100
#2)In ra cac so hoan hao tu 1 den 1000
#3)In ra chuoi finonacci tu 1 den 1000
#4)Viet ham nhap vao mot chuoi danh sach so bat ky, kiem tra xem co bao nhieu cap so trung nhau, dem so lan trung
#5)Viet class He sinh thai gom cac thuoc tinh: dong vat, thuc vat, con nguoi, tao danh sach doi tuong quan xa cua he sinh thai, dem xem co bao nhieu doi tuong cung thuoc mot loai


# 1)
# i = 2
# while i <= 100:
# 	if i%7 >0 and i%5 >0 and i%3 >0 and i%2 >0:
# 		print(i)
# 	i = i + 1

# 2)
# i = 1
# while i <= 1000:
# 	o = 0
# 	d = 0
# 	while d < i:
# 		if d%i ==0:
# 			o = o + d
# 		d = d + 1
# 	if i == o:
# 		print(i)
# 	i = i + 1

# 3)
# p = 1
# o = 1
# while o <= 1000:
# 	p = o + p
# 	print(p)
# 	o = p + o
# 	print(o)
