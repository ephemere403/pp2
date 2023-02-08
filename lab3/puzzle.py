def puzzle(numheads, numlegs):
    if(numlegs%2!=0):
        print("No answer")
    if(numheads<=numlegs/2):
        rabbits = int((numlegs / 2) - numheads)
        chicken = int(numheads - rabbits)
        print("Number of rabbits is " + str(rabbits) +". Number of chickens is " + str(chicken))
    else:
         print("No answer")
puzzle(35,94)
