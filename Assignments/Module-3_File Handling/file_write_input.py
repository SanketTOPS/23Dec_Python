fl=open("temp.txt","w")

stid=input("Enter an ID:")
stnm=input("Enter a Name:")
stct=input("Enter a City:")

"""fl.write(stid)
fl.write(stnm)
fl.write(stct)"""

fl.write(f"ID:{stid}\nName:{stnm}\nCity:{stct}")