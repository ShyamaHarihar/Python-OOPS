class A:
    def feature1(self):
        print("Feature 1 working")
    def feature2(self):
        print("Feature 2 working")
class B:
    #all methods of A can be accessed at B
    #B is subclass and A is superclass
    def feature3(self):
        print("Feature 3 is working")
    def feature4(self):
        print("Feature 4 is working")
class C(A,B):
    def feature5(self):
        print("Feature 5 is working")
a1=A()
a1.feature1()
a1.feature2()
b1=B()
c1=C()

''' 
Single level Inheritance where B is subclass and A is superclass
Multilevel Inheritance is where C is inheriting from B and B is inheriting from A
so C can access A and B methods 
In Multiple C can acess from A and B where A and B are not related to each other
But in Multilevel A and B were related to each other'''
