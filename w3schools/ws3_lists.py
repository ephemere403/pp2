#ws3 Lists

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# list, is [obj], obj = "" string, '' char, or int, etc

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#function append called by an object(fruits)	

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#function insert obtain two parameters (place, obj)

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#function remove applies directly on object(its name)

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#this gives us cherry

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#interval is :, so won't be 2,5 or 2-5

fruits = ["apple", "banana", "cherry"]
print(len(fruits))