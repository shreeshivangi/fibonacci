terms = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if terms <= 0:
   print("Please enter a positive integer")

elif terms == 1:
   print("Fibonacci sequence upto",terms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < terms:
       print(n1)
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1