import shelve
data = shelve . open("my data ")
data ["name"] = "sudhanshu"
data ["age "] = 22
print (data ["name"])
data.close()