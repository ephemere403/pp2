def squareGen(n):
    for i in range(n):
        yield (i+1)**2
 
"""for i in squareGen(int(input())):
  print(i)
"""

def evenGen(n):
  for i in range(0, n, 2):
    yield i+2

"""for i in evenGen(int(input())):
  print(str(i) + ", ")
"""

def Gen34(n):
  for i in range(n):
    if (num % 3 == 0 and num % 4 == 0):
      yield i

"""for i in Gen34(int(input())):
  print(i)
"""

def squares(a,b):
  while a <= b:
    yield (a)**2
    a += 1

"""for i in squares(int(input()), int(input())):
  print(i)
"""

def inversGen(n):
  for i in range(n):
    yield n-i

"""for i in inversGen(int(input())):
  print(i)
"""