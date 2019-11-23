__author__ = 'Mira Gleizer'

from scipy import *
import cv2
import MyChangePic as myC


def PicToArr(filename):
    image = myC.readImage(filename)
    img = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    height, width = img.shape
    PointList=[]
    for y in range(height):
        for x in range(width):
            if img[y, x] != 0:
                PointList.append([y, x])

    return PointList


def newfilesnames(fNames):

    part1 = 'Im_N'
    part2 = '.pgm'
    filenames = []
    filenames.append(fNames[0])
    for i in range(1, 21):
        filename = part1 + str(i) + part2
        img = myC.addContast(fNames[i])
        cv2.imwrite(filename, img)
        filenames.append(filename)
    return filenames


def readAll(filename):
    #this function read all files of images and return array of colored pixels

    fNames = filenames(filename)
    fNames = newfilesnames(fNames)
    ArrAllPic = []
    tempArr = []
    for i in range(0, 21):
        tempArr = PicToArr(fNames[i])
        ArrAllPic.append(tempArr)
    return ArrAllPic, fNames


def filenames(filename):
    # return the file names with indexes from 0 to 20

    str1 = filename
    path = ''
    str2 = ''
    part1 = ''
    part2 = ''
    fNames = [filename]
    for c in range(len(str1) - 1, 0, -1):
        if str1[c] == '/':
            for i in range (c+1):
                path = path + str1[i]
            break
        else:
            continue
    for i in range(c+1, len(str1)-1):
        if (str1[i].isdigit()  ) :
             break
        part1 = part1 + str1[i]
    for c in range(i+1, len(str1)):
        part2 = part2 + str1[c]
    for i in range(1, 21):
        str2 = path + part1 + str(i) + part2
        fNames.append(str2)

    return fNames

