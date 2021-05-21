# its a tuple
desserts = ("choc mousse", "muffin", "blackforest cake", "jamoon", "muffin")

## TIPS 
# tuples maintains insertion order
# unable to change values inside them
# allows duplicates


desserts1 = ("brownie")
desserts2 = ("brownie", )

print("type of desserts ", desserts," -  ", type(desserts)) #prints tuple
print("type of desserts1 ", desserts1," -  ", type(desserts1)) #prints string
print("type of desserts2 ",desserts2," -  ", type(desserts2)) #adding comma at end makes it a tuple so prints tuple

print("desserts[0]- ", desserts[0]) #print specific index
print("desserts[0:3]- ", desserts[0:3]) #print specific range from 0 - 2
print("len(desserts)- ", len(desserts)) #prints length
# print(desserts.append("sdhf")) #throws error

#To change value in tuple - convert them to list and change the desired value

changedTup = list(desserts2)
changedTup[0] = "suprise chocolate dessert"

print(changedTup)
print(type(changedTup)) #its stil a list


listToTuple = tuple(changedTup) # convert list to tuple
print(listToTuple)
print(type(listToTuple)) #its a tuple now

