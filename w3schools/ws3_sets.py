#ws3 Sets

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#set is {obj}

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#update is multiple addition for iterative

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
# If the item to remove does not exist, discard() will NOT raise an error