#!usr/bin/env python2
import pyperclip, os

try:
    f= open("tempInput.txt",'w')
    f.write(pyperclip.paste())
    f.close()

    status = os.system("python tempInput.txt > tempOutput.txt")
    if status:
        os.system("x=$(cat tempOutput.txt); zenity --error --text=\"Some error Occurred: $x\"");
    else:
        os.system("x=$(cat tempOutput.txt); zenity --info --text=\"$x\"");
except:
    print('Something went wrong! Can\'t tell what?')
    sys.exit(0) # quit Python
