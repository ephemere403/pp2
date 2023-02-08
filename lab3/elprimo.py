def prime(number):
   prime = True
   isprime = lambda x,y: x % y ==0
   for i in range(2,number):
        if(isprime(number,i)):
            prime = False
            break
   return prime
def prime_filter(intlist):
    list_prime = list(filter(prime,intlist))
    return list_prime

txt = "5 4 8 11 13 25 8 11"
intlist = []
splitter = txt.split(" ")
for x in splitter:
    intlist.append(int(x))
print(prime_filter(intlist))
#we using filter, lambda functions yeaa