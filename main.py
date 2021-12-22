#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import random
from sortingAlgorithms import bubbleSort,quickSort,sortedColoring,mergeSort
root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(900,600)
root.config(bg="#383838")

data = []
selectedAlgorithm = StringVar()

def drawData(data,colorArray):
    canvas.delete("all")
    if max(data)==0:
        scaledData= [x for x in data]
    else:
        scaledData = [x / max(data) for x in data]
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    for i,h in enumerate(scaledData):
        #top left corner
        x0 = i * x_width + offset + spacing
        y0 = c_height-h
        #boittom right
        x1 = (i+1) * x_width + offset
        y1 = c_height - h * 300
        canvas.create_rectangle(x0,y0,x1,y1,fill=colorArray[i])
        canvas.create_text(x0+2,y0,anchor=SW,text=str(data[i]))
    root.update_idletasks()
def generate():
    global data
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    try:
        maxVal = int(maxEntry.get())
    except:
        maxVal= 50
    try:
        sizeVal = int(sizeEntry.get())
    except:
        sizeVal=15
    if minVal > maxVal:
        minVal,maxVal = maxVal,minVal
    data = []
    for _ in range(sizeVal):
        data.append(random.randrange(minVal, maxVal))
    drawData(data,colorArray=["gray" for x in range(len(data))])

def startAlgo():
    global data
    #if menu.get()=='Quick Sort':
    #    quickSort(data,0,len(data)-1,drawData,speedScale.get())
    #    sortedColoring(data,drawData)
    if menu.get()=="Bubble Sort":
        bubbleSort(data,drawData,float(speedScale.get()))
    elif menu.get() =="Merge Sort":
        mergeSort(data,drawData,float(speedScale.get()))
        sortedColoring(data,drawData)
ui = Frame(root,width=600,height=200,bg="#3AE9DA")
ui.grid(row=0,column=0,padx=10,pady=5)
canvas = Canvas(root,width=600,height=380,bg="white")
canvas.grid(row=1,column=0,padx=10,pady=5)


Label(ui,text="Algorithm : ").grid(row=0,column=0,padx=5,pady=5,sticky=W)
menu = ttk.Combobox(ui,textvariable=selectedAlgorithm,values=['Bubble Sort','Merge Sort','Quick Sort'])
menu.grid(row=0,column=1,padx=5,pady=5)
menu.current(0)

speedScale = Scale(ui,from_=0.1,to=2.0,length=200,digits=2,resolution=0.1,orient=HORIZONTAL,label="Select Speed")
speedScale.grid(row=0,column=2,padx=5,pady=5)
Button(ui,text="Start",command=startAlgo,bg="#DD4545").grid(column=3,row=0,padx=5,pady=5)

sizeEntry = Scale(ui,from_=3,to=30,resolution=1,orient=HORIZONTAL,label="Select Size")
sizeEntry.grid(row=1,column=0,padx=5,pady=5,sticky=W)

minEntry = Scale(ui,from_=0,to=50,resolution=1,orient=HORIZONTAL,length=180,label="Select Minimum Value")
minEntry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

maxEntry = Scale(ui,from_=10,to=100,resolution=1,orient=HORIZONTAL,length=200,label="Select Maximum Value")
maxEntry.grid(row=1,column=2,padx=5,pady=5,sticky=W)

Button(ui,text="Generate",command=generate,bg="#DD45B0").grid(column=3,row=1,padx=5,pady=5)

root.mainloop()
