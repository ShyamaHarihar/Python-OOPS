'''
overloading same name but difference in number of parameters
not there in python
'''
'''
method overriding two methods with same name and same param in diff class with inheritance
'''
#This is method overloading
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
s1=Student(58,69)
print(s1.sum(5,9,6))