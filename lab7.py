a = []
num = int(input("enter number of elements"))

for i in range(0, num):
	e = int(input("enter element"))
	a.append(e)

min = 0
max = 100

for i in a: 
	sum += a[i]
	if min > a[i]:
		min = a[i]
	if max < a[i]:
		max = a[i]

average = sum / num

print("count")
