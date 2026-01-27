import re

mystr="This is Pythuon!988545646"

#x=re.findall('Py..on',mystr)
#x=re.findall('This|That',mystr)
x=re.findall('[A-Z]|[a-z]',mystr)
print(x)