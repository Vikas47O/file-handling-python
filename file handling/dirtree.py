import os

for folder, subfolders, files in os.walk(r"C:\Users\Vikas Sharma\OneDrive\Desktop\python"):

    print("FOLDER:", folder)

    print("SUBFOLDERS:", subfolders)

    print("FILES:", files)

    print("-----------------------------")