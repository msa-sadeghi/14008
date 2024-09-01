# x = input("enter a sentence:> ")
# ch = input("enter a charcter:> ")
# if ch in x:
#     print("OK")
# else:
#     print("Not Ok")

# x = ()
# a = input(":> ")
# x += (a,)
# a = input(":> ")
# x += (a,)
# a = input(":> ")
# x += (a,)
# print(x)

# greatest = x[0]
# if len(x[1]) > len(greatest):
#     greatest = x[1]
# if len(x[2]) > len(greatest):
#     greatest = x[2]
# print(greatest)

# name = input("enter a name:> ")
# print(name[::-1])

# لیست = []
# رشته_اول = input("enter :> ")
# لیست.append(رشته_اول)
# رشته_اول = input("enter :> ")
# لیست.append(رشته_اول)
# رشته_اول = input("enter :> ")
# لیست.append(رشته_اول)

# if len(لیست[0]) > 3:
#     print(tuple(لیست[0]))
# if len(لیست[1]) > 3:
#     print(tuple(لیست[1]))
# if len(لیست[2]) > 3:
#     print(tuple(لیست[2]))

# c = input(":> ")
# if c in "aeiou":
#     print("OK")

# age = int(input("> "))
# if age <= 13: 
#     print("Kid")
# elif age <= 20:
#     print("junior")
# elif age <= 60:
#     print("adult")
# else:
#     print("old")

# username = input("username: ")
# password = input("password: ")
# if username == "admin" and password == "1234":
#     print("valid")
# else:
#     print("invalid")

numbers = [input("> "), input("> "), input("> "), input("> ")]
s = 0
if numbers[0] % 2 == 0:
    s += numbers[0]
if numbers[1] % 2 == 0:
    s += numbers[1]
if numbers[2] % 2 == 0:
    s += numbers[2]
if numbers[3] % 2 == 0:
    s += numbers[3]
print(s)