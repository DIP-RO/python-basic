'''
Dictionaries are used to store data values in key:value pairs
it is a collection which is ordered,changeable and do not allow duplicate 
'''
studentInfo = {
    "Dip": {
        "location": "gournadi",
        "study": "level 3 term 1",
        "subject": "computer science",
        "id": 221-15-5666,
        "number": 1948803746
    },
    "tanu": {
        "location": "gournadi",
        "study": "level 3 term 1",
        "subject": "computer science",
        "id": 5666,
        "number": 1
    },
    "year":2024
}
print(studentInfo)
print(studentInfo["tanu"])
print(studentInfo["tanu"]["number"])

#access dictionaries
print(studentInfo["year"])

x= studentInfo.get("year")
print(x)
y = studentInfo.keys()
print(y)
z = studentInfo.values()
print(z)

#change item
studentInfo["year"] = 2005
print(studentInfo["year"])
studentInfo.update({"year":2020})
print(studentInfo["year"])

#delete item
studentInfo.pop("tanu")
print(studentInfo)
studentInfo.popitem()
print(studentInfo)   
#del #clear function also use for delete
