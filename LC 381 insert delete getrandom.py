class RandomizedCollection:
    def __init__(self):
        self.dataList = list()
        self.valToIndexMap = {}
        
    def insert(self, val: int) -> bool:

        index_to_insert = len(self.dataList)
        self.dataList.append(val)
            
        if val not in self.valToIndexMap:
            self.valToIndexMap[val] = set()
            self.valToIndexMap[val].add(index_to_insert)

            return True

        else:

            self.valToIndexMap[val].add(index_to_insert)
            return False


    def remove(self, val: int) -> bool:
        if val in self.valToIndexMap:
            index = self.valToIndexMap[val].pop()
            if not self.valToIndexMap[val]:
                del self.valToIndexMap[val]
            
            # Swap the element with last
            lastVal = self.dataList[-1] 

            if index != len(self.dataList) - 1:
                self.dataList[index], self.dataList[-1] = self.dataList[-1], self.dataList[index]

                # Update new index of swapped element
                self.valToIndexMap[lastVal].remove(len(self.dataList) - 1)
                # Add the new index
                self.valToIndexMap[lastVal].add(index)


            # Pop the last element
            self.dataList.pop()
            
            return True

        return False
        
    def getRandom(self) -> int:
        return random.choice(self.dataList)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()