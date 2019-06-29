import math
import random as rm
from datetime import date, datetime, time
import calendar

# math functions
print(math.factorial(5))
print(math.gcd(20, 30))
print((30*45)//math.gcd(30, 45))  # for calculating the lcm
print(math.radians(180))
print(math.sin(math.radians(90)))
print(math.floor(4.66))
print(math.ceil(4.66))
print(math.pow(2, 5))
print(math.sqrt(25))
print(math.log(10, 10))
print(math.fsum([1, 2, 3, 4, 5]))  # to calculate the sum of list
print(math.pi)
print(math.tau)


# random functions
print(rm.random())
print(rm.randint(10, 20))  # 20 will be included as limit
print(rm.randrange(10))
print(rm.randrange(10, 100))  # 100 will not be included
print(rm.randrange(10, 100, 5))  # with an interval of 5


# date functions
print(date.today())
print(datetime.now())


# calendar functions
print(calendar.prcal(2019))
print(calendar.isleap(2016))
