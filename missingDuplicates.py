import random

def missingRolls(rolls, mean, n):
        
        def calcMean(listSum, nList, lenRolls, n):
                
            a = (listSum + sum(nList)) / (lenRolls + n)
            
            if a == mean:
                   return 1
            
            elif a > mean:
                   return 0
            
            elif a < mean:
                   return 2


        lenRolls = len(rolls)
        listSum = sum(rolls)

        nList = [random.randint(1, 6) for _ in range(n)]

        for i in range(n):

            while True:

                status = calcMean(listSum, nList, lenRolls, n)

                if status == 1:
                    return nList
                    
                elif status == 0 and nList[i] - 1 != 0:
                    nList[i] = nList[i] - 1

                elif status == 2 and nList[i] + 1 != 7:
                    nList[i] = nList[i] + 1

                else:
                    break
                        
        if calcMean(listSum, nList, lenRolls, n) == 1:
             return nList
        
        else:
            return []
                
                           
                           

if __name__ == "__main__":
        
        rolls = [1,5,6]

        mean = 3
        n = 4
        
        print(missingRolls(rolls, mean, n))

