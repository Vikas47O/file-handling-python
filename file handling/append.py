file = open ("file.txt" , "a")
file.write ("this is 5th line ")
file.close()

file = open ("file.txt" , "r")
content = file.read()
print(content)
file.close()