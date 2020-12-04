class Car:

    #crate variable outside init class variable
    wheels=4
    def __init__(self):
        self.mil=10
        self.com="BMW"
        #instance variables
        #as the car changes the value also changes as this can be changed
        #instance variables and class variables are two types
c1=Car()
c2=Car()
c1.mil=8
#wheels is common for all objects so class name can be used
#namespace is an area where you create and store object/variable
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)
#40