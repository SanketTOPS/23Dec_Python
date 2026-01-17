fl=open("test.txt","a")

stid=input("Enter an ID:")
stnm=input("Enter a Name:")
stct=input("Enter a City:")

fl.write(f"ID:{stid}\nName:{stnm}\nCity:{stct}")
fl.write("\n-----------\n")