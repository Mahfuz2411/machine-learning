import math as mt
 
class KMC:
    def __init__(self) -> None:
        self.__n = 0
        self.__arr = [
            ['c1',20,500],
            ['c2',40,1000],
            ['c3',30,800],
            ['c4',18,300],
            ['c5',28,1200],
            ['c6',35,1400],
            ['c7',45,1800],
        ]
        self.__k1 = self.__arr[0]
        self.__k2 = self.__arr[1]
        self.__g1 = [self.__arr[0]]
        self.__g2 = [self.__arr[1]]
        
    
    def __sqr(self, n):
        return n*n
    
    def __diff(self, arr1, arr2):
        _, x1, y1 = arr1
        _, x2, y2 = arr2
        
        return mt.sqrt(self.__sqr(x2-x1)+self.__sqr(y2-y1))
    
    def __changeValue(self, arr1, arr2):
        _, x1, y1 = arr1
        c, x2, y2 = arr2
        
        return [c, (x1+x2)/2, (y1+y2)/2]
        
    def kmc(self):
        for i in range(2, len(self.__arr)):
            nxtk = self.__arr[i]
            df1 = self.__diff(self.__k1, nxtk)
            df2 = self.__diff(self.__k2, nxtk)
            
            if df1 <= df2:
                self.__g1.append(nxtk)
                self.__k1 = self.__changeValue(self.__k1, nxtk)
            
            else:
                self.__g2.append(nxtk)
                self.__k2 = self.__changeValue(self.__k2, nxtk)
        
        print(self.__g1)
        print(self.__g2)
        
 
def main():
    ob = KMC()
    ob.kmc()
 
if __name__ == "__main__":
    main()