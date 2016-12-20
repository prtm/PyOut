#!usr/bin/env python2
import pyperclip, os, tkMessageBox
import Tkinter as tk

try:
    f= open("tempInput.txt",'w')
    f.write(pyperclip.paste())
    f.close()

    status = os.system("python tempInput.txt > tempOutput.txt 2>&1")
    with open("tempOutput.txt",'r') as myfile:
        st=myfile.read()
    
    root = tk.Tk()
    root.withdraw() # hiding the root window
    
    if status:
	tkMessageBox.showwarning("Error Message", st)
        #os.system('x=$(cat tempOutput.txt); zenity --error --text="Some error Occurred: "'+'"'+st+'"')
    else:
	tkMessageBox.showinfo("Output", st)
        #os.system("x=$(cat tempOutput.txt); zenity --info --text=\"$x\"")
except:
    print('Something went wrong! Can\'t tell what?')
    sys.exit(0) # quit Python


""" 
    lines = []
    with open('tempOutput.txt','r') as infile:
        for line in infile:
            line = line.replace('"', '\"').replace(" ","_").replace("\n","_")
            lines.append(line)
            print line
    with open('tempOutput.txt', 'w') as outfile:
        for line in lines:
            outfile.write(line)
"""
