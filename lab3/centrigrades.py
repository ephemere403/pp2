def FtoC(farhenheit):
    centrigrades = (5/9)*(farhenheit-32) 
    return centrigrades
farhenheit = int(input("Type in Farhenheit: "))
print(FtoC(farhenheit))