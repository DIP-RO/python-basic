#user defined function
def sum(a,b):
    sum1 = a+b
    sum2 = a-b
    print(sum1)
    print(sum2)


sum(20,30)

#recursion
def runfun():
    print("dip")
    runfun()

#runfun()

#zip function
dip = ["dip","tan"]
t = ["p","s"]
print(list(zip(dip,t)))

#lambda function
x = lambda a,b:a+b
print(x(50,50))
