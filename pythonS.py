#!usr/bin/env python2
import pyperclip, os

#exec(pyperclip.paste())
f= open("tempInput.txt",'w')
f.write(pyperclip.paste())
f.close()

x=os.system("python tempInput.txt > tempOutput.txt")
try:
    os.system("leafpad tempOutput.txt");
    

except:
    print('Something went wrong! Can\'t tell what?')
    sys.exit(0) # quit Python