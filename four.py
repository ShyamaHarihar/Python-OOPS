#class methods and static methods
class Student:
    school='Amrita'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def getSchool(cls):
        print(cls.school)
    @staticmethod
    def info():
        print("This is Student class ")
        #no class avriable and instance variable static methods
        #decorator starts with @
s1=Student(34, 89, 56)
s2=Student(45, 67, 100)
print(s2.average())
print(Student.getSchool())
Student.info()
#Accessors and Mutators
#class methods for class variables
