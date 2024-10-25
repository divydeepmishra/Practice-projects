def main():
    x = int(input("What is your Number? "))
    ₹if x == 0:
        print("Neither odd nor even")
    elif is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

#or we can write––
#def is_even(n):
#   return True if n % 2 == 0 else False
#   instead of above 4 line code

#or we can write––
#def is_even(n):
#   return n % 2 == 0

main()

