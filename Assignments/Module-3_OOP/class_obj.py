class studinfo:
    stid=101
    stnm="Nirav"
    
    def getsum(self,a,b):
        print("Sum:",a+b)
    
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

st=studinfo()
st.getsum(12,34)
st.getdata(101,'Ashok')