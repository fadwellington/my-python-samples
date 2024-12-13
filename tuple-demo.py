myTuple = (1, 5, 8, 12, 29) #declare and instantiate tuple
myTuple1 = myTuple

print("Accessing elements example: " + str(myTuple[1]) +"\n") # will access the second element in the tuple

print("Negative Index example: " + str(myTuple[-3]) + "\n") # will access third element in the tuple (5 - 3)

myList = list(myTuple) # creating a list and assigning it the values of myTuple
myList.pop() # removes the element at the end of the list
myTuple = tuple(myList) # replaces myTuple with new updated tuple
print("New tuple: " + str(myTuple))
print("Original tuple: " + str(myTuple1))
