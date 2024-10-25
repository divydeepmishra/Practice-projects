n = 0
where = input("Go left or right? ")
while where == "right" :
    n = n + 1
    if n > 2:
        print(":(")
    where = input("Go left or right? ")
print("You go out!")







x = float(input("What is x? "))
y = float(input("What is y? "))
z = round(x + y)
print(f"{z:,}")







x = int(input("x: "))
y = int(input("y: "))
z = x / y
print(f"{z:.5f}")








s = input()
print(s.lower())








n = input()
m = n.replace(" ", "...")
print(m)








before = input("Before: ")
print("After: ", end="")

#Another Example-
print(before.upper())
for i in range(10):
    print("meaow")
