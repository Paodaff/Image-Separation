__author__ = 'Mira Gleizer'


import cv2
import funfiles as ff
from PIL import Image

def readImage(filename):
   # Try to read in an image file, errors out if we can't find the file
    img = cv2.imread(filename)
    if img is None:
        print('I can not find the file:  ' + filename)
        return None
    else:
        return img


def myRGB2GRAY (img):
    if img is not None:
        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        elif len(img.shape) == 4:
            gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
    return gray


def addContast(filename):
    img = readImage(filename)
    myImage = myRGB2GRAY (img)
    height, width = myImage.shape
    for y in range(height):
        for x in range(width):
            if myImage[y, x] != 0:
                myImage[y, x] = myImage[y, x] * 20
    return myImage



def compareArrImg(tempArr, img, SumI):
    for j in tempArr:
        y = j[0]
        x = j[1]
        sum1 = img[y, x, 0] + img[y, x, 0] + img[y, x, 2]
        if sum1 < 3:
            return False
    return True


def notinFnames(fnames, fname):
    for i in fnames:
        if i == fname:
            return False
    return True


def FindTopXY(img,  h,  w):
    for y in range(h):
        for x in range(w):
            if img[y, x] != 0:
                return y, x, img[y, x]


def FindPic(filename):
    img = readImage(filename)
    gray = myRGB2GRAY(img)
    cv2.imwrite('myimg.png', img)
    myImage = readImage('myimg.png')
    height, width = gray.shape
    ImgW = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    NewImg = []
    count = 0
    fnames = []
    ArrAllPic, fNames = ff.readAll(filename)

    while count < 10:
        flag = 0
        y, x, sum2 = FindTopXY(ImgW, height, width)

        for i in range(1, 21):
            if ArrAllPic[i][0] == [y, x]:
                if compareArrImg(ArrAllPic[i], img, sum2) and notinFnames(fnames, fNames[i]):
                    count = count + 1
                    print 'count ', count
                    fname = fNames[i]
                    fnames.append(fname)
                    print 'fname  ', fname
                    flag = 1
                    ImgW = DeleteFoundImage(ArrAllPic[i], sum2, ImgW)
        if flag == 0 and ImgW[y, x] != 0:
            NewImg.append([y, x])
            sum1 = ImgW[y, x]
            if sum1 == sum2:
                ImgW[y, x] = 0
            elif sum1 > sum2:
                ImgW[y, x] = ImgW[y, x] - 1

    for y in range(height):
        for x in range(width):
            if ImgW[y, x] != 0:
                NewImg.append([y, x])
                ImgW[y, x] = 0
    for i in fnames:
         ChangeFoundImg(i)
    for y in range(height):
        for x in range(width):
            if [y,x] in NewImg:
                myImage.itemset((y, x, 0), 0)
                myImage.itemset((y, x, 1), 255)
                myImage.itemset((y, x, 2), 0)
            else:
                myImage.itemset((y, x, 0), 255)
                myImage.itemset((y, x, 1), 255)
                myImage.itemset((y, x, 2), 255)
    cv2.imwrite('NotListedImg.pgm', myImage)
    fNames.append('NotListedImg.pgm')
    fname = changeOriginaltoRed(fNames[0], NewImg)
    cv2.imwrite('BlendofRedImg.pgm', fname)
    fNames.append('BlendofRedImg.pgm')
    return myImage, fNames


def DeleteFoundImage (tempArr, SumI, ImgW):

    for j in tempArr:
        y = j[0]
        x = j[1]

        if ImgW[y, x] == 1:
            ImgW[y, x] = 0

        elif ImgW[y, x] > 1:
            ImgW[y, x] = ImgW[y, x] - 1

    return ImgW

def ChangeFoundImg(filename):
    image = Image.open(filename)
    img = ChangeColor(filename)
    cv2.imwrite(filename, img)
    return filename


def ChangeColor(filename):
    img = readImage(filename)
    gray = myRGB2GRAY(img)

    height, width = gray.shape
    finalImg = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

    flag = 0
    for y in range(height):
       for x in range(width):
           for i in range(0,3):
                if img[y,x, i] != 0 :
                    finalImg.itemset((y, x, 0), 0)
                    finalImg.itemset((y, x, 1), 0)
                    finalImg.itemset((y, x, 2), 255)
                    flag = 1
                    break
                else:
                    continue
           if flag == 0:
                for i in range(0, 3):
                    finalImg.itemset((y, x, i), 255)
           flag = 0
    return finalImg

def changeOriginaltoRed (filename, NewImg):
    img = readImage(filename)
    Image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    height, width = Image.shape

    finalImg = cv2.cvtColor(Image, cv2.COLOR_GRAY2RGB)

    for y in range(height):
        for x in range(width):
            if [y,x] in NewImg:
                finalImg[y, x, 0] = finalImg[y, x, 0] - 1
                finalImg[y, x, 1] = finalImg[y, x, 1] - 1
                finalImg[y, x, 2] = finalImg[y, x, 2] - 1

    flag = 0
    for y in range(height):
        for x in range(width):
            color = finalImg[y, x, 0] + finalImg[y, x, 1] + finalImg[y, x, 2]
            if color != 0:
                #print color
                finalImg.itemset((y, x, 0), 255 - color * 10)
                finalImg.itemset((y, x, 1), 255 - color * 10)
                finalImg.itemset((y, x, 2), 255)
                flag = 1
            if flag == 0:
                for i in range(0, 3):
                    finalImg.itemset((y, x, i), 255)
            flag = 0
    return finalImg

