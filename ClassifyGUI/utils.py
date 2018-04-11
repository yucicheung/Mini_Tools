import os
import tkinter as tk
import tkinter.messagebox

def checkdir(pathToCheck):
    if not os.path.isdir(pathToCheck):
        os.mkdir(pathToCheck)
        return 0
    else:
        return len(os.listdir(pathToCheck))


def checkSourceEmpty(picList):
    if len(picList)==0:
        tk.messagebox.showwarning(title='Finish', message='Finish processing all images of this type!')
        return False
    else:
        return True
