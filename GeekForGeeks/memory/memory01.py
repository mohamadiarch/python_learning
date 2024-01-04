x=10
y=x

print(id(x))
print(id(y))

x=20
print(id(x))
print(id(y))
# Python doesn't have explicit assignment by reference like some languages
# we can not use something like this in python ==> x=&y

