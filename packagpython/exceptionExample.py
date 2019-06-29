# # doubtful lines can be put in try block
# # the exception messages will be in except block we can specify specific EXCEPTION CLASS
#
#
# def div():
#     a = [1, 2, 3, 4]
#     try:
#         num1 = eval(input("ENTER NUM 1 : "))
#         num2 = eval(input("ENTER NUM 2 : "))
#         rem = num1 // num2
#         print("Remainder is ", rem)
#         print("Number at index", a[rem])
#
#     except NameError:
#         print("Wrong input")
#         div()
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#         div()
#     except IndexError:
#         print("Index out of range")
#         div()
#     except:
#         print("it can handle all error")
#     else:  # it runs when try block completely runs
#         print("It runs when try block executes")
#     finally:  # it will run always mainly used ot close the connections made
#         print("It runs always")
#
#
# print("*****************WELCOME****************\n")
# div()
# print("*****************THANK YOU****************")


def div(a, b):
    try:
        print("Tyr block")
        c = a/b
        return c
    except:
        print("Exception Block")
        return 1
    else:
        print("Else Block")
        return 2
    finally:
        print("Finally Block")
        # return 3
    print("End of Div")


print(div(5, 0))
