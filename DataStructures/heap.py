import math

class Heap:
    def __init__(self, arr, minHeap=True, removeDuplicates=True, visualize=False):
        '''
        Need to prevent some of these attributes from being changed
        '''
        self.heapArr = []
        self.minHeap = minHeap
        self.removeDuplicates = removeDuplicates
        self.elements = {}
        self.visualize = visualize
        self.createHeap(arr)

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

    def createHeap(self, arr):
        for num in arr:
            self.add(num)

    def add(self, element):
        if self.removeDuplicates and self.elements.get(element):
            pass
        else:
            self.elements[element]=1
            ind = len(self.heapArr)
            self.heapArr.append(element)
            self.heapify(ind)

    def heapify(self, ind):
        parent = (ind-1)//2
        if parent >= 0:
            if self.minHeap and self.heapArr[parent] > self.heapArr[ind]:
                self.heapArr[parent], self.heapArr[ind] = self.heapArr[ind], self.heapArr[parent]
                self.heapify(parent)
            elif (not self.minHeap) and self.heapArr[parent] < self.heapArr[ind]:
                self.heapArr[parent], self.heapArr[ind] = self.heapArr[ind], self.heapArr[parent]
                self.heapify(parent)
        if self.visualize:
            print(self)

    def delete(self, element):
        pass

    def max(self, k=1):
        if not self.minHeap:
            return self.kthFromTop(k)
        else:
            return self.kthFromBottom(k)

    def min(self, k=1):
        if self.minHeap:
            return self.kthFromTop(k)
        else:
            return self.kthFromBottom(k)

    def kthFromTop(self, k):
        ans = [None for i in range(k)]
        queue = [0]
        while len(queue):
            ind = queue.pop(0)
            if ind < len(self.heapArr):
                val = self.heapArr[ind]
                for i in range(k):
                    num = ans[i]
                    if val == num:
                        child1 = 2*ind+1
                        child2 = 2*ind+2
                        queue.append(child1)
                        queue.append(child2)
                        break
                    if (not num) or (self.minHeap == (val < num)):
                        ans.insert(i, val)
                        ans.pop()
                        child1 = 2*ind+1
                        child2 = 2*ind+2
                        queue.append(child1)
                        queue.append(child2)
                        break
        return ans[-1] if ans[-1] else ans[0]

    def kthFromBottom(self, k):
        ans = [None for i in range(k)]
        n = len(self.heapArr)
        row = math.ceil(math.log(n+1, 2))
        startInd = 2**(row-1)-1
        queue = [i for i in range(startInd, n)]
        while len(queue):
            ind = queue.pop(0)
            if ind >= 0:
                val = self.heapArr[ind]
                for i in range(k):
                    num = ans[i]
                    if val == num:
                        parent = (ind-1)//2
                        if (len(queue) == 0) or (queue[-1] != parent):
                            queue.append(parent)
                        break
                    if (not num) or (self.minHeap != (val < num)):
                        ans.insert(i, val)
                        ans.pop()
                        parent = (ind-1)//2
                        if (len(queue) == 0) or (queue[-1] != parent):
                            queue.append(parent)
                        break
        return ans[-1] if ans[-1] else ans[0]

    def sort(self):
        pass

def test():
    arr = [5,6,3,2,1,5,7,8,3,4,5,1,2,3,10,15,13,12,11,4,3,2,11]
    myHeap = Heap(arr, minHeap=False, removeDuplicates=False)#, visualize=True)
    myHeap.add(4)
    print(myHeap)
    print(myHeap.min())
    print(myHeap.max())
    print(myHeap.max(2))
    print(myHeap.max(3))
    print(myHeap.max(6))
    print(myHeap.max(10))
    print(myHeap.min(3))
    print(myHeap.min(10)) # returns the first min if input k exceeds number of unique elements
    # need to think about what happens if input arr is empty or not array, handle bad input in general
    # print doesn't work if numbers are multiple digits
    # need to fix kthFromBottom to add elements that have no children, if bottom row isn't full

test()
