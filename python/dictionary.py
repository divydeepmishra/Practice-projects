a = {"key": "value", "harry": "code","marks": "100", "list": [1,3,5,]}

#print(a.items())

#print(a.keys())

#print(a.get("marks"))

a.update({"friends": "divy"})

print(a)













people = {
    "Careter": "+1234555",
    "David": "+12345344",
    "John": "+12349403",
}
name = input("Name: ")
if name in people:
        number = people[name]
        print(f"Found {number}")
else:
    print("Not found")

