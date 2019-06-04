from PIL import Image
import glob
import countPixels
from os.path import basename
import os
import re
import math
import operator

class FontStruct():
    def __init__(self, picture,style,number):
        self.picture = picture
        self.style = style
        self.number = number
        self.generalPercent = countPixels.GeneralBlackPixels(picture)
        self.leftPercent = countPixels.LeftBlackPixels(picture)
        self.rightPercent = countPixels.RightBlackPixels(picture)
        self.upPercent = countPixels.UpBlackPixels(picture)
        self.downtPercent = countPixels.DownBlackPixels(picture)

def loadData():
    imageList = []
    r = re.compile("([a-zA-Z]+)([0-9])")
    for filename in glob.glob('D:\Python\шрифти\класи\*.jpg'):   
        im=Image.open(filename)
        filename=os.path.splitext(basename(filename))[0]
        m = r.match(filename)
        imageList.append(FontStruct(im,m.group(1),m.group(2)))
    testImage=FontStruct(Image.open('D:\Python\шрифти\Test2.jpg'),'', -1)
    return testImage,imageList

def getDistance(object1,object2):
    distance=0
    distance+=math.pow(object1.generalPercent-object2.generalPercent,2)
    distance+=math.pow(object1.leftPercent-object2.leftPercent,2)
    distance+=math.pow(object1.rightPercent-object2.rightPercent,2)
    distance+=math.pow(object1.upPercent-object2.upPercent,2)
    distance+=math.pow(object1.downtPercent-object2.downtPercent,2)
    return math.sqrt(distance)

def getNeighbors(imageList, testImage, k):
    distancesList=[]
    for image in imageList:
        distancesList.append((image,getDistance(image,testImage)))
    distancesList.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
    	neighbors.append(distancesList[x][0])
    return neighbors

def main():
    testImage,imageList=loadData()   
#    n=getNeighbors(imageList, testImage, 10)
    numb=[]
    for i in getNeighbors(imageList, testImage, 20):
        numb.append(i.style)
    print('Test Image is from class:'+max(set(numb), key=numb.count))

main()


            
         