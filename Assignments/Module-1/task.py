fullname=input("Enter your fullname:")
if fullname.isalpha():
    print("Your Name:",fullname)
    
    email=input("Enter an Email:")
    if email.islower():
        print("Your Email:",email)
        
        password=input("Enter your password:")
else:
    print("Error!Invalid input...")
        
