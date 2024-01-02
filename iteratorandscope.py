list = [1,2,3,4,5,"dip","hablu"]
for i in list:
    print(i)
#single single output iterate ...list iterable
#now use iter() method and next() method
x= iter(list)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(next(x))

#global scope and local scope
a = 30 #global

def dip():
    x = 100 #local
    print(x)
    print(a)
dip()

#global keyword