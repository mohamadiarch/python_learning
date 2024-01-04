

a=45
b=0
c=True

if b and a or c:
    print("true")
else:
    print("false")

print("-------------")

if c or a and b:
    print("first")
else:
    print("two")

print("-------------")


if b:
    print("b",type(b))
