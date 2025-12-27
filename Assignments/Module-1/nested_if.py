a=int(input("Enter number1:"))
b=int(input("Enter number2:"))

if a!=0 and b!=0: #parent - root
    if a<b: #child
        print("Sum:",a+b)
    else:
        print("Mul:",a*b)
else:
    print("Error!Invalid number")
        