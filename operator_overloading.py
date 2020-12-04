'''
Operator and Operands
add integer and float
add integer
add strings
methods for operators behind the scene
'''
#a='5'
#b='6'
#print(a+b)
#print(str.__add__(a,b))
class Student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+self.m2
        m2=other.m1+other.m2
        s3=Student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
    #overriding str
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)
s1=Student(58,66)
s2=Student(60,65)
s3=s1 + s2
print(s3.m1)
if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")
print(s3)#this without the method prints the address but when
#how will python know what is + here before they belong to int or str class
#now it is a user defined class
'''
Same method name but number of arguments or type of arguments are different
'''