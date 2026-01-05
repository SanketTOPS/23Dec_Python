stdata={
    'id':1,
    'name':'sanket',
    'city':'rajkot'
}

#print(stdata)
#print(stdata['name'])
#print(stdata.get('city'))
#print(stdata.keys())
#print(stdata.values())
#print(len(stdata))

"""if 'name' in stdata:
    print("Yes...")
else:
    print("Noo")"""
    
"""if 'sanket' in stdata.values():
    print("Yes...")
else:
    print("Noo")"""
    
"""for i in stdata:
    print(i)"""
    
"""for i in stdata.values():
    print(i)"""
    
"""for i in stdata.items():
    print(i)"""

"""for i,j in stdata.items():
    print(i,j)"""
    
# ------------------------------ #
print(stdata)
#stdata['id']=2
#stdata['sub']='python'
#stdata.pop('city')
#stdata.clear()

#print(stdata)

newdata=stdata.copy()
print(newdata)