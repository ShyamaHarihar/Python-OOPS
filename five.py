#nested class
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.Laptop()
        #nested class object
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    class Laptop:
        def __init__(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram=8
        def show(self):
            print(self.brand, self.cpu, self.ram)
s1=Student('Navin',2)
s2=Student('Jenny',3)
s1.show()
#lap1=s1.lap
#lap2=s2.lap
lap1=Student.Laptop()
'''inside init of main class create object of nested class and there is a 
method with same name in both classes and call the nested class method
in main class with the object created in init of main class'''