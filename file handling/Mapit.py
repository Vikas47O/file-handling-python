import webbrowser
import sys
# webbrowser.open("https://www.google.com/")
if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])
else:
    address = input("Enter location : ")
# address = input("enter location : ")
webbrowser.open("https://www.google.com/maps/place/" + address)