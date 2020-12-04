'''
Poly means many and morphism is form
Objects have multiple forms
Duck Typing
Operator Overloading
Method Overloading
Method Overriding
mention the type of object which is used in other languages diff here'''
'''Dynamic Typing is there in python where we don't specify the data type
'''
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Running')
class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
ide=MyEditor()
lap1=Laptop()
lap1.code(ide)