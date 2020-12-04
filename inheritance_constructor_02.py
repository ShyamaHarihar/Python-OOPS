class A:
    def __init__(self):
        print("in A init")
    def feature1(self):
        print("Feature 1 A")
    def feature2(self):
        print("Feature 2 working")
class B:
    def __init__(self):
        super().__init__()
        print("In B init")
    def feature1(self):
        print("Feature 1 B")
    def feature4(self):
        print("Feature 4 is working")
class C(A,B):
    #multiple inheritance where A and B are accessed
    def __init__(self):
        super().__init__()
        print("In c init")
    def feat(self):
        super().feature2()
#Method Resolution Order init of itself and then left to right
#Prefer left one
c1=C()
c1.feature1()

