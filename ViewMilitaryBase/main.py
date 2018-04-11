# -*- coding: utf-8 -*-
import webbrowser
import os
import tkinter as tk
import re

coord_file = 'coordinates'
record_file = 'log'
index = 1 # indicate which line you are at, initialized as 1

# read all coordinates from file
f = open(coord_file,'r')
contents = f.readlines()

# create log file or read from log file
if not os.path.exists(record_file):
    with open(record_file,'w') as record:
        record.write('index=1')
else:
    with open(record_file,'r+') as record:
        temp = record.readline()
        index = int(re.findall(r'\d+',temp)[0]) # get which line you were at

# set up a window
window = tk.Tk()
window.title("view military base")
window.geometry('200x200')
# initialize button message
butt_var = tk.StringVar()
butt_var.set('start viewing.')
lab_var = tk.StringVar()

# set up a label for showing
message = tk.Label(window, textvariable=lab_var, bg='light gray',)
message.pack()

# webbrowser control firfox browser
c = webbrowser.get("firefox")

def control_firefox():
    global index;global contents
    butt_var.set('next')
    content = contents[index-1]
    suffix = re.findall(r'\d+.*',content)[0]
    prefix = content[0:len(content)-suffix.__len__()-1]
    suffix_N,suffix_W = re.split('N',suffix)
    suffix_N = suffix_N +'N'
    suffix = suffix_N+'+'+suffix_W
    lab_var.set('viewing pic ' + str(index) +' :'+prefix)
    url = 'http://www.google.com/maps/place/'+suffix
    c.open_new_tab(url)
    index += 1
    with open(record_file,'w') as record:
        record.write('index='+str(index))

view_butt = tk.Button(window,textvariable=butt_var,width=15,height=2,command=control_firefox)
view_butt.pack()
control_firefox()

window.mainloop()
