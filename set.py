#set items are unchangeable, but you can remove or add new items
#it not support duplicate value
#a set is a collection which is unordered ,unchangeable,unindexed
myset = {1,2,True , "string"}
print(type(myset))
print(myset)
print(len(myset))


#access set items
yset = {1,2,3,4,5}
for i in yset:
    print(i)

print(1 in yset)

#add set items
x = {'DIP','TANU','alu','hera','esha'}
x.add('shuv')
print(x)

#add any iterable(the obj in the update() method does not have to be a set,it can be any iterable obj(tuples,lists,dictionaries)etc)
yset.update(x)
print(yset)

h = [6,7,8]
yset.update(h)
print(yset)

#if we use remove function it will give error if element is not found but discard will not ggive any error
#remove set items
x.remove('shuv')
print(x)
x.discard('DIP')
print(x)
#using pop you dont know which item that gets removed
x.pop()
print(x)
x.clear()
print(x)


#loop sets
k = {'DIP','TANU','alu','hera'}
for i in k:
    print(i)

#join sets
set3 = {'DIP','TANU','alu','hera'}
set4 = {1,2,3}
set5 = set3.union(set4)
print(set5)
set4.update(set3)
print(set4)

#methods
"""
add()
clear()
copy()
difference()
difference_update()
discard()
intersection()
intersection_update()
isdisjoint()
issubset()
issuperset()
pop()
remove()
etc. source(w3school)

"""