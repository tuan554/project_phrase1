def tong(n):
	total = 0
	i = 1
	while i <= n:
		total = total + i
		i = i + 1
	return total
# print(tong(10))
def mult(n):
	total = 0
	i = 1
	v = 2
	while i <= n:
		total = total + i**v
		i = i + 1
	return total
# print(mult(3))
def fraction(n):
	total = 1
	i = 1
	v = 2
	while v <= n:
		total = total + i/v
		v = v + 1
	return total
#print(fraction(3))
def evenFra(n):
	total = 1
	i = 2
	while i <= n:
		total = total + total/i
		i = i + 2
	return total
# print(evenFra(4))
def oddFra(n):
	total = 1
	i = 3
	while i <= n:
		total = total + total/i
		i = i + 2
	return total
# print(oddFra(4))
def B6(n):
	total = 0
	i = 2
	v = 1
	while v <= n:
		total = total + 1/v*i
		v = v + 1
		i = i + 1
	return total
# print(B6(3))
def B7(n):
	total = 0
	v = 1
	i = 2
	while v <= n:
		total = total + v/i
		v = v + 1
		i = i + 1
	return total
# print(B7(4))
def B8(n):
	total = 0
	v = 1
	i = 2
	while v <= n:
		total = total + v/i
		v = v + 2
		i = i + 2
	return total
# print(B8(3))
def B9(n):
	total = 1
	i = 2
	while i <= n:
		total = total*i
		i = i + 1
	return total
# print(B9(3))
def sq(n, x):
	dem = 2
	i = n
	while dem <= x:
		n = n * i
		dem = dem + 1
	if x == 0:
		n = 1
	return n
# print(sq(2, 0))


def x(i):
# 	v = 2
# 	r = 1
# 	o = 1
# 	while v <= i:
# 		o = o*v
# 		r = r + o
# 		v = v + 1
# 	return r
	o = 0
	t = 1
	while t <= i:
		o = o + B9(t)
		t = t + 1
	return o
#print(x(4))
def B2(x, i):
	# o = 0
	# r = 1
	# while r <= i:
	# 	r = x**r
	# 	o = o + r
	# return o
	o = 0
	r = 1
	while r <= i:
		o = o + sq(x, r)
		r = r + 1
	return o
# print(B2(2, 4))
def B20(i):
	o = 1
	while o <= i:
		if i%o == 0:
			print (o)
		o = o + 1
#print(B20(10))
def B21(i):
	o = 1
	t = 0
	while o <= i:
		if i%o == 0:
			t = t + o
		o = o + 1
	return t
#print(B21(4))
def B28(i):
	o = 1
	t = 0
	while o < i:
		if i%o == 0:
			t = t + o
		o = o + 1
	return t
#print(B28(6))
def B50(n):
	e = str(n)
	d = len(e)-1
	h = ''
	while d >= 0:
		h = h + e[d]
		d = d - 1
	return int(h)
# print(B50(123456789))
def B51(n):
	h = 0
	e = str(n)
	d = 0
	while d < len(e):
		if h < int(e[d]):
			h = int(e[d])
		d = d + 1
	return int(h)
# print(B51(12378228374))
def B59(n):
	e = str(n)
	d = len(e)-1
	h = ''
	while d >= 0:
		h = h + e[d]
		d = d - 1
	if int(h) == n:
		print("True")
	else:
		print("False")
# print(B59(121))	
def B62(a, b):
	d = 1
	g = b
	if a < b:
		g = a
	l = 0 
	while d <= g:
		if a % d == 0:
			if b % d == 0:
				l = d
		d = d + 1
	return l
print(B62(100, 50))




















