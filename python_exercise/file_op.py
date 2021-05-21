readFile = open("sample.txt") # second param represents r(read), w(write), x(create)

print(readFile.read())
#readline prints only one line
# print(readFile.read(10)) #reads first 10 chars, 
# cannot call read method twice on same file

print(readFile.readline()) # prints only first line
print(readFile.readline()) # prints second line
readFile.close()


#open a file in write mode and edit dtat
writeFile = open("sample.txt", "w")
writeFile.write("This is a sample file updated using python")
writeFile.close()

#read updated data in file
readChangedFile = open("sample.txt")
print(readChangedFile.read())
readChangedFile.close()


#create a new file and write some data

createFile = open("NewFile.txt", "w") # creates a newfile if it doesnt exists already
createFile.write("this file is created using write more param since its not present already")
createFile.close()

#to delete a file

import os
os.remove("NewFile.txt")

#check if file exists using path parameter and then delete

if os.path.exists("NewFile.txt"):
  os.remove("NewFile.txt")

