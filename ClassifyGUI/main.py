# -*- coding: utf-8 -*-
from ClassifyGUI import ClassifyGUI
import os

# config vars
config = {}
config["destinationDir"] = './dataset'
config["searchPathList"] = ['./dataset/hm','./dataset/hz','./dataset/ys',
                            './dataset/jq']
config["types"] = ["AircraftCarrier",'Bomber','TransportAircraft','DestroyerAndFrigate']
config["dumpPath"] = [os.path.join(config["destinationDir"], config["types"][i] + 'Dump') for i in xrange(4)]
config["picSize"] = (500, 500)
config["windowTitle"] = 'Classify pics'
config["windowGeometry"] = '900x750'


if __name__=="__main__":
    ClassifyGUI(config)
