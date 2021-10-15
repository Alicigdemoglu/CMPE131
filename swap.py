 # Swap the first and last member

def swap_last_item(inputList):
    #take the first elements store it in a variable and swap
    temp = inputList[0]
    inputList[0] = inputList[-1]
    inputList[-1] = temp
     
    return inputList
   #test 
#print(swap_last_item([8, 5 ,5 ,7 ,9]))