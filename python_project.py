from tkinter import *
import os.path
import math
from tkinter.filedialog import *
from tkinter.simpledialog import *
import struct

## 함수 선언부
def loadImage(fname):
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB,inW,inH,outW,outH,window,canvas,paper,filename

    photo = PhotoImage(file=filename)
    inW = photo.width()
    inH = photo.height()

    for i in range(inH) :
        tmpList=[]
        for k in range(inW) :
            tmpList.append(0)
        inImageR.append(tmpList[:])
        inImageG.append(tmpList[:])
        inImageB.append(tmpList[:])


    for i in range(inH):
        for k in range(inW):
            r,g,b = photo.get(k,i)
            inImageR[i][k] = r
            inImageG[i][k] = g
            inImageB[i][k] = b
    photo = None

    equal()


def display():
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename

    if canvas != None:
        canvas.destroy()

    window.geometry(str(outH)+'x'+str(outW))
    canvas = Canvas(window,width=outW, height=outH)
    paper =PhotoImage(width=outW, height =outH)
    canvas.create_image((outW/2,outH/2),image=paper,state='normal')

    for i in range(outH):
        for k in range(outW):
            dataR = outImageR[i][k]
            dataG = outImageG[i][k]
            dataB = outImageB[i][k]
            paper.put("#%02x%02x%02x" % (dataR,dataG,dataB),(k,i))
        canvas.pack()

def exitFile():
    window.quit()
    window.destroy()

def openFile():
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageV,inW,inH,outW,outH,window,canvas,paper,filename
    filename = askopenfilename(parent=window, filetypes=(("그림파일", "*.gif"), ("모든파일", "*.*")))
    loadImage(filename)
    equal()

def equal() : # 동일 영상 알고리즘 구현
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW; outH = inH;
    for i in range(outH) :
        tmpList=[]
        for k in range(outW) :
            tmpList.append(0)
        outImageR.append(tmpList[:]) # 리스트 복사 [:]
        outImageG.append(tmpList[:])
        outImageB.append(tmpList[:])
    for i in range(inH) :
        for k in range(inW):
            outImageR[i][k] = inImageR[i][k]
            outImageG[i][k] = inImageG[i][k]
            outImageB[i][k] = inImageB[i][k]
    display()

def saveFile():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb',
                               defaultextension="*.gif", filetypes=(("Gif파일", "*.gif"), ("모든파일", "*.*")))
    for i in range(outW):
        for k in range(outH):
            saveFp.write(struct.pack('B', outImage[i][k]))

    saveFp.close()


################# 화소점 처리 #####################
def addImage() :
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW; outH = inH;
    for i in range(outH) :
        tmpList=[]
        for k in range(outW) :
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    value = askinteger('밝게하기', '밝게할 값-->', minvalue=1, maxvalue=255)
    for i in range(inH) :
        for k in range(inW):
            if inImageR [i][k] * value > 255 :
                outImageR[i][k] = 255
            elif inImageG [i][k] * value > 255 :
                outImageG[i][k] = 255
            elif inImageB[i][k] * value > 255 :
                outImageB[i][k] = 255
            else :
                outImageR[i][k] = inImageR[i][k] + value
                outImageG[i][k] = inImageG[i][k] + value
                outImageB[i][k] = inImageB[i][k] + value

    display()

def multiplyImage() : # 영상 곱하기 알고리즘
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW; outH = inH;
    for i in range(outH) :
        tmpList=[]
        for k in range(outW) :
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    value = askinteger('밝게 곱하기', '밝게할 값-->', minvalue=1, maxvalue=255)
    for i in range(inH) :
        for k in range(inW):
            if inImageR [i][k] * value > 255 :
                outImageR[i][k] = 255
            elif inImageG [i][k] * value > 255 :
                outImageG[i][k] = 255
            elif inImageB[i][k] * value > 255 :
                outImageB[i][k] = 255
            elif inImageR[i][k] * value < 0 :
                outImageR[i][k] = 0
            elif inImageG[i][k] * value < 0 :
                outImageG[i][k] = 0
            elif inImageB[i][k] * value < 0 :
                outImageB[i][k] = 0
            else :
                outImageR[i][k] = inImageR[i][k] * value
                outImageG[i][k] = inImageG[i][k] * value
                outImageB[i][k] = inImageB[i][k] * value

    display()

def decreaseImage() :
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW; outH = inH;
    for i in range(outH) :
        tmpList=[]
        for k in range(outW) :
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    value = askinteger('어둡게빼기', '어둡게할 값-->', minvalue=1, maxvalue=255)
    for i in range(inH) :
        for k in range(inW):
            if inImageR[i][k] - value < 0 :
                outImageR[i][k] = 0
            elif inImageG[i][k] - value < 0 :
                outImageG[i][k] = 0
            elif inImageB[i][k] - value < 0 :
                outImageB[i][k] = 0
            else :
                outImageR[i][k] = inImageR[i][k] - value
                outImageG[i][k] = inImageG[i][k] - value
                outImageB[i][k] = inImageB[i][k] - value

def divisionImage() : # 영상 나누기 알고리즘
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW; outH = inH;
    for i in range(outH) :
        tmpList=[]
        for k in range(outW) :
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    value = askinteger('어둡게나누기', '어둡게할 값-->', minvalue=1, maxvalue=255)
    for i in range(inH) :
        for k in range(inW):
            if  inImageR [i][k] // value > 255 :
                outImageR[i][k] = 255
            elif inImageG [i][k] // value > 255 :
                outImageG[i][k] = 255
            elif inImageB[i][k] // value > 255 :
                outImageB[i][k] = 255
            elif inImageR[i][k] // value < 0 :
                outImageR[i][k] = 0
            elif inImageG[i][k] // value < 0 :
                outImageG[i][k] = 0
            elif inImageB[i][k] // value < 0 :
                outImageB[i][k] = 0
            else :
                outImageR[i][k] = inImageR[i][k] // value
                outImageG[i][k] = inImageG[i][k] // value
                outImageB[i][k] = inImageB[i][k] // value

    display()
#########################################################

#############기하학 처리 ###################
def upDown() :  # 상하 반전 알고리즘
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW;  outH = inH;
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImageR[outW-1-i][k] = inImageR[i][k]
            outImageG[outW-1-i][k] = inImageG[i][k]
            outImageB[outW-1-i][k] = inImageB[i][k]
    display()

def leftRight() :  #좌우  반전 알고리즘
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    outW = inW;  outH = inH;
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            outImageR[i][outW-1-k] = inImageR[i][k]
            outImageG[i][outW-1-k] = inImageG[i][k]
            outImageB[i][outW-1-k] = inImageB[i][k]
    display()


def panImage() : # 화면이동
    global  panYN
    panYN = True

def mouseClick(event) :  # 화면클릭
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    global sx, sy, ex, ey, panYN
    if not panYN :
        return
    sx = event.x;  sy = event.y;

def mouseDrop(event):  # 화면 놓기
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    global sx, sy, ex, ey, panYN
    if not panYN:
        return
    ex = event.x; ey = event.y;
    my = sx - ex ; mx = sy - ey
    outW = inW;  outH = inH;
    for i in range(outH):
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
            if 0<= i-mx <outH and 0<= k-my < outW :
                outImageR[i-mx][k-my] = inImageR[i][k]
                outImageG[i-mx][k-my] = inImageG[i][k]
                outImageB[i-mx][k-my] = inImageB[i][k]
    panYN = False
    display()



def zoomOut() :  # 축소하기 알고리즘
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    # 중요! 출력메모리의 크기를 결정
    scale = askinteger('축소하기', '축소할 배수-->', minvalue=2, maxvalue=32)
    outW = int(inW/scale);  outH = int(inH/scale);
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
             outImageR[int(i/scale)][int(k/scale)] = inImageR[i][k]
             outImageG[int(i/scale)][int(k/scale)] = inImageG[i][k]
             outImageB[int(i/scale)][int(k/scale)] = inImageB[i][k]
    display()

def zoomIn() :  # 확대하기 알고리즘
    global inImageR,inImageG,inImageB,outImageR,outImageG,outImageB, inW, inH, outW, outH, window, canvas, paper, filename
    scale = askinteger('확대하기', '확대할 배수-->', minvalue=2, maxvalue=32)
    outW = int(inW*scale);  outH = int(inH*scale);
    for i in range(outH):  # 출력메모리 확보(0으로 초기화)
        tmpList = []
        for k in range(outW):
            tmpList.append(0)
        outImageR.append(tmpList)
        outImageG.append(tmpList)
        outImageB.append(tmpList)
    for  i  in  range(inH) :
        for  k  in  range(inW) :
             outImageR[int(i*scale)][int(k*scale)] = inImageR[i][k]
             outImageG[int(i*scale)][int(k*scale)] = inImageG[i][k]
             outImageB[int(i*scale)][int(k*scale)] = inImageB[i][k]
    display()

#######################################


## 전역 변수 선언부
inImageR,inImageG,inImageB,outImageR,outImageG,outImageB,=[],[],[],[],[],[]
inW,inH,outW,outH =[0]*4
window,canvas,paper,filename = [None]*4
panYN = False;  sx, sy, ex, ey = [0] * 4

## 메인 코드부
window = Tk();
window.title("영상 처리 & 데이터 분석 Ver 0.05")


mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일',menu=fileMenu)
fileMenu.add_command(label='열기',command=openFile)
fileMenu.add_command(label='저장',command=saveFile)
fileMenu.add_command(label='종료',command=exitFile)

pixeMenu= Menu(mainMenu)
mainMenu.add_cascade(label='화소점처리',menu=pixeMenu)
pixeMenu.add_command(label='동일영상',command=equal)
pixeMenu.add_command(label='밝게더하기',command=addImage)
pixeMenu.add_command(label='밝게곱하기',command=multiplyImage)
pixeMenu.add_command(label='어둡게빼기',command= decreaseImage)
pixeMenu.add_command(label='어둡게나누기',command=multiplyImage)

GeometryMenu= Menu(mainMenu)
mainMenu.add_cascade(label='기하학처리',menu=GeometryMenu)
GeometryMenu.add_command(label='상하반전',command=upDown)
GeometryMenu.add_command(label='좌우반전',command=leftRight)
GeometryMenu.add_command(label='화면이동',command=panImage)
GeometryMenu.add_command(label='축소하기',command=zoomOut)
GeometryMenu.add_command(label='확대하기',command=zoomIn)

window.mainloop()