"""data=[]
stdata={}

n=int(input("Enter number of students:"))
for i in range(n):
    id=input("Enter an ID:")
    name=input("Enter a Name:")
    stdata["id"]=id
    stdata["name"]=name
    data.append(stdata)
    
print(data)
"""

stdata={}
n=int(input("Enter number of students:"))

for i in range(n):
    stid=int(input("Enter an ID:"))
    name=input("Enter a Name:")
    city=input("Enter a City:")
    
    stdata[stid]={"name":name,"city":city}

#print(stdata)
for i in stdata.items():
    print(i)
    