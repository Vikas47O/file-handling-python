import zipfile
# connect two things 
names = ( "Vikas" , "Dhruv", "Dev")
laptop = ( "Infinix" , "Asus", "Lenovo")

zipped = list(zip(names , laptop))
print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)
