import re

username=input("Enter an Username:")

username_pattern="[A-Z]+[a-z]+[0-9]"

x=re.findall(username_pattern,username)

if x:
    print("Username is valid!")
else:
    print("Error!Invalid Username...")