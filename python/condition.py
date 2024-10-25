m = int(input())
n = int(input())
o = int(input())
p = int(input())

if m>n>o>p:
    print(m)
elif m<n>o>p:
    print(n)
elif m<n<o>p:
    print(o)
else:
    print(p)








s = "abca"
seen =''
for char in s:
    if char not in seen:
        seen = seen + char

print(len(seen))








s = "demo loops - How are you?"
for char in s:
    if char == 'h' or char == 'y':
        print("There is a h or y")







x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y"))
if x == y:
    print("x and y are equal")
    if y != 0:
        print("therefore, x/y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
print("Thanks")








s = 25
n = int(input("Guess the Number: "))
if n == s:
    print("Same as our secret number")
elif n > s:
    print("Higher than our Number")
else:
    print("Lower than our Number")
print("thank you")









username = input()
if len(username) < 10:
    print("less than 10")
elif len(username) > 10:
    print("more than 10")
else:
    print("equal to 10")










s1 = int(input())
s2 = int(input())
s3 = int(input())
t = (s1+s2+s3)/300
t = t * 100
if s1 >= 33 and s2 >= 33 and s3 >= 33 and t >= 40:
    print("Pass")
else:
    print("Fail")










from cs50 import get_int
x = get_int("What's x? ")
y = get_int("What's y? ")
if x < y:
    print("x is less than y")
elif x > y:
    print("x is gretaer than y")
else:
    print("x is equal to y")










import sys

if len(sys.argv) != 2:
    print("Missing command line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)









from sys import argv

if len(argv) == 2:
    print(f"hello,{argv[1]}")
else:
    print("hello, world\n")

