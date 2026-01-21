class Student:
    # Constructor (__init__ method) gets called automatically when an object is created
    def __init__(self):
        print("Constructor called!")
        self.stid = 0
        self.stnm = ""

    # Parameterized Constructor
    def create_student(self, stid, stnm):
        self.stid = stid
        self.stnm = stnm

    def printdata(self):
        print("ID:", self.stid)
        print("Name:", self.stnm)

# Creating first object
# The constructor is called here
st1 = Student() 
st1.create_student(101, "Sanket")
st1.printdata()

print("-" * 20)

# Creating second object
st2 = Student()
st2.create_student(102, "Rohan")
st2.printdata()
