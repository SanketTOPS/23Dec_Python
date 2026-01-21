class hitesh:
    hid:int
    htech:str
    
    def h_getdata(self):
        self.hid=input("Enter Hitesh's ID:")
        self.htech=input("Enter Hitesh's Tech.:")

class mitesh(hitesh):
    mid:int
    mtech:str
    
    def m_getdata(self):
        self.mid=input("Enter Mitesh's ID:")
        self.mtech=input("Enter Mitesh's Tech.:")
        
class ashok(mitesh):
    aid:int
    atech:str
    
    def a_getdata(self):
        self.aid=input("Enter Ashok's ID:")
        self.atech=input("Enter Ashok's Tech.:")

class tops(ashok):
    def printdata(self):
        print("------Hitesh's Data-------")
        print("Hitesh's ID:",self.hid)
        print("Hitesh's Tech:",self.htech)
        print("------Mitesh's Data-------")
        print("Mitesh's ID:",self.mid)
        print("Mitesh's Tech:",self.mtech)
        print("------Ashok's Data-------")
        print("Ashok's ID:",self.aid)
        print("Ashok's Tech:",self.atech)

tp=tops()
tp.h_getdata()
tp.m_getdata()
tp.a_getdata()
tp.printdata()