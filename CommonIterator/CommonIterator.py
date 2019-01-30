"""
Lyft Coding Interview
Problem Statement:
Create a class CommonIterator that takes in two iterator objects. The next()
function of this class should return the next common element between the two
iterators. The hasNext() function of this class should return a boolean value
stating whether or not a next common element exists. The input iterators are
assumed to contain integers sorted in ascending value.
"""
class CommonIterator:
    def __init__(self, t1, t2):
        self.t1 = t1
        self.t2 = t2
        self.nextAns = None

    def next(self):
        if self.nextAns:
            tmp = self.nextAns
            self.nextAns = None
            return tmp

        a = next(self.t1, None)
        b = next(self.t2, None)

        while a and b:
            if a > b:
                b = next(self.t2, None)
            elif a < b:
                a = next(self.t1, None)
            else:
                return a
        return None

    def hasNext(self):
        if self.nextAns:
            return True
        else:
            tmp = self.next()
            if tmp:
                self.nextAns = tmp
                return True
            else:
                return False

iter1 = iter([1,4,6,7,8])
iter2 = iter([1,2,3,4,5,7,9])
iterCommon = CommonIterator(iter1, iter2)

print(iterCommon.next()) # 1
print(iterCommon.hasNext()) # True
print(iterCommon.hasNext()) # True
print(iterCommon.next()) # 4
print(iterCommon.hasNext()) # True
print(iterCommon.next()) # 7
print(iterCommon.hasNext()) # False
print(iterCommon.next()) # None
print(iterCommon.hasNext()) # False
print(iterCommon.next()) # None
print(iterCommon.hasNext()) # False
