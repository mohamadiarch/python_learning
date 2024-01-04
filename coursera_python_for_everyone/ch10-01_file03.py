

a={"name":"ali","age":45,"country":"iran"}
print(a)
b=a.items()
print(b)

# dict.items make a list of tuppels
for value in b:
    print(value)
    for k in value:
        print(k,"k")

# tupples can itterate


# we can get (k,v) or just use a variable
# both gets the same
for (k,v) in b:
    print(k,v)
