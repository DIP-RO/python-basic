class ParentInfo:
    def eshanfamily(self, name, age):
        print(f"my name is {name}, my age is {age}")

p1 = ParentInfo()
p1.eshanfamily("eshan", 19)

#constructor with parameter
class ParentInfo:
    def __init__(self,name , number):
        print(f"my name is {name} and age is {number}")

p1 = ParentInfo("eshan", 19)

#instance method and class method and static method
class classname:
    def instancemethod(self):
        print("hello instance method")
    
    @classmethod
    def classMethod(cls):
        print("this is class method")
    @staticmethod
    def staticmethod():
        print("this is static method")
v1 = classname()
v1.instancemethod()
#classname.instancemethod()
v1.classMethod()
classname.classMethod()

v1.staticmethod()
classname.staticmethod()


#abstruction
#polymorphism
class Vehicle:
    def __init__(self , model , brand , component):
        self.model = model
        self.brand = brand
        self.component = component
class BMW(Vehicle):
    pass
class Rangerover(Vehicle):
    pass
x = BMW("hybusa" , "bmw" , "chaaka")
z = Rangerover("range" , "rover" , "baaka")
print(x.brand)
print(z.brand)