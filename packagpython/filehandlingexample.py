# FILE HANDLING

# # to write
# fp = open("Bijin.txt", "a")
# name = input("ENTER NAME")
# mob = input("ENTER MOB")
#
# data = name + ":" + mob + "\n"
#
# print(data)
#
# fp.write(data)
# fp.close()


# to read
# there is a very important concept of cursor
# whenever the file read the cursor goes to that position
# and then next read will start form that point
# so we have to use the seek() to move the cursor
fp = open("Bijin.txt", "r")
print(fp.read())
fp.seek(0, 0)
print(fp.read(5))
fp.seek(0, 0)
print(fp.readlines())
fp.seek(0, 0)
print(fp.readline())
print(fp.readline())
