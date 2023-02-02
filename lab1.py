a = []
a = input()
print("enter multiple variables" + a)

min = 0
max = 100

for i in a: 
	count += 1
	sum += a[i]
	if min > a[i]:
		min = a[i]
	if max < a[i]:
		max = a[i]

average = sum / count

print("count")
