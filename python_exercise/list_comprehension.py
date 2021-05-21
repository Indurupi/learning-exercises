list = ["apple", "kiwi", "pinaple", "pome"]
newList = []

# without list comprehension
for x in list:
  if "a" in x:
    newList.append(x)

print(newList)

# with list comprehension
newLists = [x for x in list if "i" in x] #returns item x from list if i is present i the xth item

print(newLists)

newLists = [x for x in range(10)] #returns from 0 to 9

print(newLists)

newLists = [x if x > 5 else "beyond" for x in range(10) ] #returns if x is greater than 5 prints x else prints beyond

print(newLists)