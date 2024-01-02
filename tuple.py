#tuple immutable
mytuple = ("apple" ,"dip","tanu", "moye-moye" ,"pagol")
#access
print(mytuple[1])
#negative indexing
print(mytuple[-1])
#range of index
print(mytuple[1:3])


#update tuple(first convert tuple to list,then again convert list to tuple)
mytuple1 = list(mytuple)
mytuple1.append("org")
mytuple = tuple(mytuple1)
print(mytuple)


#unpack tuple
dip = ("bana","mana","sana")
(a , b , c) = dip
print(a)
(*b,c) = dip
print(b)
print(c)


#loops in tuple
dip1 = ("bana","mana","sana")
for i in dip1:
    print(i)

for x in range(len(dip1)):
    print(x)
    print(dip1[x])

y=0
while y<len(dip1):
    print(dip1[y])
    y = y+1



#join tuple
    tuple1 = (1,2,3,4,4)
    tuple2 = ('dip','mui')
    tuple3 = tuple1 + tuple2
    print(tuple3)

    #multiply tuple:
    tuple4 = tuple2 * 2
    print(tuple4)
#count
    z = tuple1.count(4)
    print(z)
#index
    v = tuple1.index(3)
    print(v)