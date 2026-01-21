class studinfo:
    stid:int
    stnm:str
    fl=open("stdata.txt","a")
    
    def getst(self):
        n=int(input("Enter number of students:"))
        
        for i in range(n):
            self.stid=input("Enter an ID:")
            self.stnm=input("Enter a Name:")
            
            self.fl.write(f"ID:{self.stid}")
            self.fl.write(f"\nName:{self.stnm}")
            self.fl.write(f"\n-----------------\n")
            self.fl.close()
    
    def printdata(self):
        self.fl=open("stdata.txt",'r')
        print(self.fl.read())
        
st=studinfo()

print("1:Insert Data")
print("2:Read Data")
choice=int(input("Enter your choice:"))

if choice==1:
    st.getst()
elif choice==2:
    st.printdata()
        