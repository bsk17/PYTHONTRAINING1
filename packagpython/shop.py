import math

products = []

x=3


def entry():
   for k in range(3):
       print("Enter for sales", k)
       a = eval(input("Enter Quantity"))
       b = eval(input("Enter Quantity"))
       c = eval(input("Enter Quantity"))

       products.append([a, b, c])

entry()

n = 0

for i, j, k in products:
    print("%4d%4d%4d%4d"%(i, j, k, int(math.fsum(products[n]))))
    n = n + 1

sum1 = 0
sumList = []
for i in range(3):
    for j in range(3):
        sum1 = sum1 + products[j][i]
    sumList.append(sum1)
    sum1 = 0

sum2 = math.fsum(sumList)
sumList.append(sum2)

for i in sumList:
    print("%4d"%i, end="")