class Dip:
    name = ""#property
    number = ""

a = Dip() #obj
a.name = "T"
print(a.name)

#inheritance
class baba:
    car = "BMW"
    tk = "100cr"
    home = "2 building"

class sela(baba):
    phone ="1 ta"

y = sela()
print(y.car)

#multiple inheritance
class parent:
    car ="1 ta"
class parent2:
    home ="1 ta"
class parent3:
    bankaccount ="1 ta"
class ami(parent , parent2 , parent3):
    mobile = "1ta"
x = ami()
print(x.car)

#multilevel inheritance
class Baba_ma:
    car ="1 ta"
class son1(Baba_ma):
    home ="1 ta"
class son2(son1):
    bankaccount ="1 ta"
class son3(son2):
    mobile = "1ta"
z = son3()
print(z.car)

#hybrid and hierarchical inheritance


