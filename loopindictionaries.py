#loop in dictionaries
studentInfo = {
    "Dip": {
        "location": "gournadi",
        #"study": "level 3 term 1",
        #"subject": "computer science",
        #"id": 221-15-5666,
        "number": 1948803746
    },
    "tanu": {
        "location": "gournadi",
       # "study": "level 3 term 1",
        #"subject": "computer science",
        #"id": 5666,
        "number": 1
    },
    "year":2024
}

for i in studentInfo:
    print(i)
for x in studentInfo.values():
    print(x)
for y in studentInfo.keys():
    print(y)
for a, b in studentInfo.items():
    print(a,b)

#copy dictionaries
mydix = studentInfo.copy()
print(mydix)

v = dict(studentInfo)
print(v)