import pandas

stdata={
    'id':[101,102,103,104],
    'name':['sanket','amol','vaibhav','rohan'],
    'city':['rajkot','surat','mumbai','pune']
}

dt=pandas.DataFrame(stdata)
print(dt)