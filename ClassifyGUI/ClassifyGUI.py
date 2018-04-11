# -*- coding: utf-8 -*-
from utils import *
import os
from PIL import Image, ImageTk

class ClassifyGUI():
    def __init__(self, config):
        self.config = config
        self.radioButtonPos = (100,150)
        self.imgBoxPos = (200,200)
        self.radioPad = 220
        self.gridPad = (30,10)
        self.setUpWindow()


    def setUpWindow(self):
        searchPathLists = self.config["searchPathList"]
        picLists = [[p for p in os.listdir(searchPathLists[i]) if p.endswith('.png')] for i in xrange(4)]
        destinationDir = self.config["destinationDir"]
        types = self.config["types"]
        dumpPaths = self.config["dumpPath"]


        def radioButtonTrigger():

            Index = pathIndex.get()
            processPath = searchPathLists[Index]
            picList = picLists[Index]
            if checkSourceEmpty(picList):
                destinationPath = os.path.join(destinationDir, types[Index])
                checkdir(destinationPath)
                checkdir(dumpPaths[Index])
                picpath = os.path.join(processPath, picList[-1])
                changeImg(picpath)


        def buttonTrigger0():
            typeIndex = 0
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                type = types[typeIndex]
                searchPathList = searchPathLists[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(destinationDir, type, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)

        def dumpTrigger0():
            typeIndex = 0
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                searchPathList = searchPathLists[typeIndex]
                dumpPath = dumpPaths[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(dumpPath, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)

        def buttonTrigger1():
            typeIndex = 1
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                type = types[typeIndex]
                searchPathList = searchPathLists[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(destinationDir, type, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)

        def dumpTrigger1():
            typeIndex = 1
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                searchPathList = searchPathLists[typeIndex]
                dumpPath = dumpPaths[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(dumpPath, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)
        def buttonTrigger2():
            typeIndex = 2
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                type = types[typeIndex]
                searchPathList = searchPathLists[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(destinationDir, type, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)

        def dumpTrigger2():
            typeIndex = 2
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                searchPathList = searchPathLists[typeIndex]
                dumpPath = dumpPaths[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(dumpPath, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)
        def buttonTrigger3():
            typeIndex = 3
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                type = types[typeIndex]
                searchPathList = searchPathLists[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(destinationDir, type, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)

        def dumpTrigger3():
            typeIndex = 3
            picList = picLists[typeIndex]
            if checkSourceEmpty(picList):
                processImg = picList.pop()
                searchPathList = searchPathLists[typeIndex]
                dumpPath = dumpPaths[typeIndex]
                srcImg = os.path.join(searchPathList, processImg)
                desImg = os.path.join(dumpPath, processImg)
                os.system('mv {} {}'.format(srcImg, desImg))
                if checkSourceEmpty(picList):
                    picpath = os.path.join(searchPathList, picList[-1])
                    changeImg(picpath)


        def changeImg(imgPath):
            print imgPath
            im = Image.open(imgPath)
            processImage = ImageTk.PhotoImage(im)
            lbPic['image'] = processImage
            lbPic.image = processImage


        window = tk.Tk()
        window.title(self.config["windowTitle"])
        window.geometry(self.config["windowGeometry"])
        lbPic = tk.Label(window, text='image', width=500, height=500)
        lbPic.place(x=self.imgBoxPos[0], y=self.imgBoxPos[1], width=500, height=500)

        # set up radio buttons
        pathIndex = tk.IntVar()
        for i in xrange(4):
            tk.Radiobutton(window, text=self.config["searchPathList"][i], variable=pathIndex,
                           value=i, command=radioButtonTrigger).\
                place(x=self.radioButtonPos[0]+self.radioPad*i,y=self.radioButtonPos[1],anchor='nw')


        for i in xrange(2):
            for j in xrange(4):
                if i%2 == 0:
                    tk.Button(window, text=self.config["types"][j], width=20, height=1,
                            command=eval('buttonTrigger'+str(j))).\
                        grid(row=i, column=j, padx=self.gridPad[0], pady=self.gridPad[1])
                elif i % 2 == 1:
                    tk.Button(window, text='dump '+self.config["types"][j], width=20, height=1,
                              command=eval('dumpTrigger'+str(j))). \
                        grid(row=i, column=j, padx=self.gridPad[0], pady=self.gridPad[1])

        window.mainloop()
