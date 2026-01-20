class studinfo:
    stid=12
    stnm="Sanket"
    
    def myfunc(self):
        print("This is myfunc.")


st=studinfo() #object of class
print(st.stid)
print(st.stnm)
st.myfunc()