import itertools
from math import factorial

#i don't know how to actually do it else, and how to defend it tomorrow:)

def permutations(txt):
    chars = list(txt)
    permutations = list(itertools.permutations(chars))
    permutations_list = []
    print("The amount of permutations of string " + txt + " is " + str(factorial(len(txt))))
    print("Permutations for "+ txt +" are")
    for i in permutations:
        res = ""
        for j in i:
            res += j
        permutations_list.append(res)
    return permutations_list


print(permutations("jana"))