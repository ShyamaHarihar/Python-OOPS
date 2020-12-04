class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B(A):
    #all methods of A can be accessed at B
    #B is subclass and A is superclass
    def __init__(self):
        super().__init__()
        print("In B init")
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")

b1=B()
'''
So if subclass has init then that will be called else superclass init will be 
called for object of class B where single level inheritance is being implemented
To call init of A and B a super method is used'''