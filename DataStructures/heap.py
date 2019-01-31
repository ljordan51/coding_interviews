import math

class Heap:
    def __init__(self, arr, minHeap=True, removeDuplicates=True, visualize=False):
        self.heapArr = []
        self.minHeap = minHeap
        self.duplicates = {}
        self.visualize = visualize
        self.max = None
        self.min = None
        self.createHeap(arr, removeDuplicates)

    def __repr__(self):
        n = len(self.heapArr)
        rows = math.ceil(math.log(n+1, 2))
        returnString = ''
        for i in range(rows):
            row = i+1
            printString = ''
            padding = 2**(rows-row)-1
            for pad in range(padding):
                printString = printString + ' '
            betweenString = ''
            between = 2**(rows-i)-1
            for btw in range(between):
                betweenString = betweenString + ' '
            startInd = 2**(row-1)-1
            endInd = n if row == rows else 2**row-1
            for ind in range(startInd, endInd):
                num = self.heapArr[ind]
                if num < 0:
                    printString = printString[:-1]
                printString = printString + str(num) + betweenString
            returnString = returnString + printString + '\n'
        return returnString

    def createHeap(self, arr, removeDuplicates):
        for num in arr:
            if removeDuplicates and self.duplicates.get(num):
                continue
            else:
                self.duplicates[num]=1
                self.add(num)

    def add(self, element):
        ind = len(self.heapArr)
        self.heapArr.append(element)
        self.heapify(ind)

    def heapify(self, ind):
        parent = (ind-1)//2
        if parent >= 0:
            if self.minHeap and self.heapArr[parent] > self.heapArr[ind]:
                self.heapArr[parent], self.heapArr[ind] = self.heapArr[ind], self.heapArr[parent]
                if self.visualize:
                    print(self)
                self.heapify(parent)
            elif (not self.minHeap) and self.heapArr[parent] < self.heapArr[ind]:
                self.heapArr[parent], self.heapArr[ind] = self.heapArr[ind], self.heapArr[parent]
                self.heapify(parent)

    def delete(self, element):
        pass

    def max(self, k):
        pass

    def min(self, k):
        pass

    def sort(self):
        pass

def test():
    arr = [5,6,3,2,1,5]#,7,8,3,4,5,1,2,3,10,15,13,12,11,4,3,2,11]
    myHeap = Heap(arr)#, minHeap=False, removeDuplicates=False, vi)
    myHeap.add(4)
    print(myHeap)

test()
