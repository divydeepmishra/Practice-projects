#i = 0
#while i < 5:
 #   print("Divy")
  #  i = i + 1






#for i in range (0,10):
 #   print(i)
  #  if i==5:
  #      break







#for i in range(4):
 #   print("printing")
 #   if i == 2:
  #      continue
  #  print(i)






#n = int(input("Enter your number: "))
#i = 1
#while i <= 10:
 #   print(n*i)
  #  i += 1






#l = ["Harry","Soham","Sachin","Rahul"]
#for items in l:
 #   print("Hello", items)






#l = ["Harry","Soham","Sachin","Rahul"]
#for items in l:
 #   if (items.startswith("S")):
  #    print("Hello", items)






#n = int(input("Enter Number: "))
#for i in range (2, n):
 #  if (n%i == 0):
  #    print("Number is not prime")
   #   break
#else:
 #  print("Number is prime")






#n = int(input("Enter Number: "))
#i = 1
#sum = 0
#while i <= n:
  #  sum += i
   # i = i + 1
#print(sum)






#n = int(input("Enter Number: "))
#product = 1
#for i in range(1, n+1):
#    product = product*i
 #   i +=1
#print(product)






#n = int(input("Enter Number: "))
#i = 1
#f = 1
#while i <= n:
 #   f *= i
 #   i += 1
#print(f"the factorial of {n} is {product}")






#n = int(input("Enter Number: "))
#for i in range(1, n+1):
 #       print("*" * i, end="")
 #       print("")






#n = int(input("Enter Number: "))
#for i in range(1,11):
#    print(f"{n} X {11-i} = {n*(11-i)}")






#even_nums = 0
#for i in range(10):
 #   if i % 2 == 0:
 #       even_nums += 1
#print(even_nums)








#s = int(input())
#for i in range(1, s+1):
 #   print(str(i)*s)









from cs50 import get_int

#while True:
    #n = get_int("Height: ")
    #if n>0:
      #  break

#for i in range(n):
    #print("#")
#print()

for i in range(3):
    for j in range(3):
        print("#", end="")
    print()


