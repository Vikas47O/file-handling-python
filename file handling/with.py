# with open ("file.txt", "r") as file:
#     content = file.read()
#     print(content)

file = open("file.txt", "r")
print(file.closed)
file.close()
print(file.closed)

with open("file.txt", "r") as file:
    print(file.closed)
print(file.closed)
