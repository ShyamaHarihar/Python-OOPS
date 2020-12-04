#Python supports all paradigms - functional,procedural and object oriented
#functional programming - pass functions inside a function etc
#procedural programming - everything is written explicitly
#object and class together class is a design/blueprint and object is an instance
#class keyword followed by name then collon
#attributes and behaviours/methods/functions
class Computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        #self is used to call the object and the passed arguments are assigned
        #to initialise the variables
        #called automatically
        print("in init")
        #called for every object that is created
    def config(self):
        print("Config is",self.cpu,self.ram)
com1=Computer('i5',16)#com1 is an object of Computer
com2=Computer('Ryzen 3',8)#com2 is an object of Computer
print(type(com1))#str is a class inbuilt and computer is user defined
#int is also class
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()
#not passing any param in second way we are calling it with object so behind the scene
#it automatically passes the object into the method
#com1 is the object passed for self parameter
#objects are used to call methods because every object has different data
