import ascii_magic , sys
from termcolor import *

img = input('enter image name or path : ')
chars = input('\nenter char like # or * etc : ')
file_text = input('\nenter text file name : ')

if img == "" or file_text =="" or chars == "":
	print (colored("[-_-] sorry enter info correct","red"))
elif "txt" in file_text:
    output = ascii_magic.from_image_file(img,columns=50,char=chars)
    words = ascii_magic.to_terminal(output)
    with open(f"{file_text}","a") as ascii_art :
        print(output, file = ascii_art)
else:
    output = ascii_magic.from_image_file(img,columns=50,char=chars)
    words = ascii_magic.to_terminal(output)
    with open(f"{file_text}.txt","a") as ascii_art :
        print(output, file = ascii_art)