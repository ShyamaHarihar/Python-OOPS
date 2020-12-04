#init is a constructor
class Computer:
    def __init__(self):
        self.name="Navin"
        self.age=28
    def update(self):
        self.age=30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False
c1=Computer()
c2=Computer()


if c1.compare(c2):
    print("They are same")
#compare takes two parameters self is c1 and other is c2
c1.name="Rashi"
c1.update()#calling it is okay but no paramter is passed self is a pointer
#self will point to c1 points to current instance
#c1 is referencing to object heap memory has objects
print(c1.name)
print(c2.name)
#every time object is created new memory is allocated
#size depends on no of variables
#constructor is responsible
#address of memory