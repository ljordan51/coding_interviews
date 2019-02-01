import time
import random
"""
Amazon Coding Interview 1/29/2019 10AM PST
Problem Statement:
Find third max of non-empty unsorted array with duplicates
If no kth max, return 1st max (aka regular max or just max)
Follow up question related to flexibilty if we wanted to find a different kth max (such as fourth or second)
"""
def thirdMax(arr, k):
    """
    My answer
    Time complexity: O(kn)
    Space complexity: O(k)
    """
    maxes = [None for i in range(k)]
    for num in arr:
        for i in range(len(maxes)):
            max = maxes[i]
            if num == max:
                break
            elif max == None or num > max:
                maxes.insert(i, num)
                maxes.pop()
                break
    return maxes[-1] if maxes[-1] else maxes[0]

def thirdMaxTime(arr, k):
    start = time.time()
    ans = thirdMax(arr, k)
    end = time.time()
    #print(ans)
    return end-start

def thirdMaxHeap(arr, k):
    """
    Answer using heap
    Time complexity: O(nlogn)
    Space complexity: O(n)
    The interviewer asked me to implement a heap O(nlogn) to solve this problem
    I didn't feel comfortable implementing a heap but now I've learned and done it below
    He weirdly specifically mentioned a min-heap which I didn't really understand because a max-heap
    seems more efficient considering k is likely to be small relative to n in most practical cases
    """
    def heapify(heap, i):
        if i > 0:
            parent = (i-1) // 2
            if heap[i] > heap[parent]:
                heap[i], heap[parent] = heap[parent], heap[i]
                heapify(heap, parent)

    def findKthMax(heap, k):
        queue = [0]
        maxes = [None for i in range(k)]
        while len(queue):
            ind = queue.pop(0)
            if ind < len(heap):
                val = heap[ind]
                for i in range(len(maxes)):
                    max = maxes[i]
                    if max == None or val > max:
                        maxes.insert(i, val)
                        maxes.pop()
                        child1 = 2*ind+1
                        child2 = child1+1
                        queue.append(child1)
                        queue.append(child2)
                        break
        return maxes[-1] if maxes[-1] else maxes[0]

    maxHeap = []
    duplicates = {}
    for num in arr:
        if not duplicates.get(num):
            duplicates[num] = 1
            maxHeap.append(num)
            heapify(maxHeap, len(maxHeap)-1)
    if k >= len(maxHeap):
        return maxHeap[0]
    return findKthMax(maxHeap, k)

def thirdMaxHeapTime(arr, k):
    start = time.time()
    ans = thirdMaxHeap(arr, k)
    end = time.time()
    #print(ans)
    return end-start


# arrs = [[i for i in range(100000)], [-i+99999 for i in range(1000000)], [1,3,4,7,8,3,2,4,5,1], [1,2]]
# arrs = [[1,3,4,7,8,3,2,4,5,1], [1,2]]
arrs = []
maxInt = 1000
lenLists = [10, 100]#, 1000, 10000, 100000, 1000000, 10000000, 100000000]
numLists = len(lenLists)
for i in range(numLists): # generate 10 lists of length 10000 containing integers in range 0-1000
    lenList = lenLists[i]
    arrs.append([int(maxInt*random.random()) for j in range(lenList)])
# print(arrs)
myTotal, heapTotal = 0, 0
k = 2
iterations = 30
avgTimes = []
for arr in arrs:
    for i in range(iterations):
        myTime = thirdMaxTime(arr, k)
        myTotal = myTotal + myTime

        heapTime = thirdMaxHeapTime(arr, k)
        heapTotal = heapTotal + heapTime
    avgTimes.append([myTotal/iterations, heapTotal/iterations, len(arr)])
print(avgTimes)
