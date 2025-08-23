class RandomizedSet:
    import random
    def __init__(self):
        self.dataList = list()
        self.valToIndexMap = {}
        
    def insert(self, val: int) -> bool:

        # When element not already in list, add to end of list and map the index
        if val not in self.valToIndexMap:
            index = len(self.dataList)
            self.valToIndexMap[val] = index
            self.dataList.append(val)

            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.valToIndexMap:
            index = self.valToIndexMap[val]
            
            # Swap the element with last
            lastVal = self.dataList[-1] 

            self.dataList[index], self.dataList[-1] = self.dataList[-1], self.dataList[index]

            # Update new index of swapped element
            self.valToIndexMap[lastVal] = index

            # Pop the last element
            self.dataList.pop()
            self.valToIndexMap.pop(val)

            return True

        return False
        
    def getRandom(self) -> int:
        return random.choice(self.dataList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()