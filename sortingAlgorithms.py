import time
def bubbleSort(data,draw,timeTick):
    times = [x/10 for x in range(20,0,-1)]
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data [j+1]:
                data[j], data[j+1] = data[j+1],data[j]
                draw(data,["cyan" if x==j or x == j + 1 else 'gray' for x in range(len(data))])
                time.sleep(times[int(timeTick*10)-1])
    sortedColoring(data,draw)
def sortedColoring(data,draw):
    colors = ["gray" for i in range(len(data))]
    for i in range(len(data)):
        colors[i] = "cyan"
        draw(data,colors)
        time.sleep(0.1)
    time.sleep(0.2)
    colors = ["gray" for i in range(len(data))]
    draw(data,colors)
    time.sleep(0.5)
    colors = ["cyan" for i in range(len(data))]
    draw(data,colors)
    time.sleep(0.5)
    colors = ["gray" for i in range(len(data))]
    draw(data,colors)
    time.sleep(0.5)
    colors = ["cyan" for i in range(len(data))]
    draw(data,colors)
    time.sleep(0.5)
    colors = ["gray" for i in range(len(data))]
    draw(data,colors)
def partition(data,head,tail,draw,timeTick):
    times = [x/10 for x in range(20,0,-1)]
    border = head
    pivot = data[tail]
    draw(data,getColorForQuickSort(len(data),head,tail,border,border))
    time.sleep(times[int(timeTick*10)-1])
    for j in range(head,tail):
        if data[j] < pivot:
            draw(data,getColorForQuickSort(len(data),head,tail,border,j,isSwaping=True))
            time.sleep(times[int(timeTick*10)-1])
            data[border], data[j] = data[j],data[border]
            border+=1
        draw(data,getColorForQuickSort(len(data),head,tail,border,j))
        time.sleep(times[int(timeTick*10)-1])
    draw(data,getColorForQuickSort(len(data),head,tail,border,j,True))
    time.sleep(times[int(timeTick*10)-1])
    data[border], data[tail] = data[tail], data[border]
    return border
def quickSort(data,head,tail,draw,timeTick):
    if head<tail:
        partitionIndex = partition(data,head,tail,draw,timeTick)
        quickSort(data,head,partitionIndex-1,draw,timeTick)
        quickSort(data,head,partitionIndex+1,draw,timeTick)
def getColorForQuickSort(dataLen,head,tail,border,currI,isSwaping=False):
    colorArray = []
    for i in range(dataLen):
        if i>= head and i<= tail:
            colorArray.append('cyan')
        else:
            colorArray.append("gray")
        if i == tail:
            colorArray[i] = "blue"
        elif i==border:
            colorArray[i] ="red"
        elif i==currI:
            colorArray[i] ="yellow"
        if isSwaping:
            if i==border or i ==currI:
                colorArray[i] ="green"

def mergeSort(data,draw,timeTick):
    times = [x/10 for x in range(20,0,-1)]
    if len(data) > 1:
        mid = len(data)//2
        leftSection = data[:mid]
        rightSection = data[mid:]
        mergeSort(leftSection,draw,timeTick)
        mergeSort(rightSection,draw,timeTick)
        i = j = k = 0
        while i<len(leftSection) and j < len(rightSection):
            if leftSection[i] < rightSection[j]:
                draw(data,["cyan" if x ==i or x==k else "gray" for x in range(len(data))])
                data[k] = leftSection[i]
                time.sleep(times[int(timeTick*10)-1])
                i+=1
            else:
                draw(data,["cyan" if x ==j or x==k else "gray" for x in range(len(data))])
                data[k] = rightSection[j]
                time.sleep(times[int(timeTick*10)-1])
                j+=1
            k+=1
        while i< len(leftSection):
            draw(data,["cyan" if x ==i or x==k else "gray" for x in range(len(data))])
            data[k] = leftSection[i]
            time.sleep(times[int(timeTick*10)-1])
            i+=1
            k+=1
        while j<len(rightSection):
            data[k] = rightSection[j]
            time.sleep(times[int(timeTick*10)-1])
            draw(data,["cyan" if x ==j or x==k else "gray" for x in range(len(data))])
            j+=1
            k+=1
