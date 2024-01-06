a={"name":"mohammad","age":45}

# print(a[0])   # gets error 
# a."nest"=45    # gets error
# print(a.name)   # gets error
print(a["name"])

a["name"]={"fisrt":"nima","last":"mohanadi"}
print(a)
print(a["name"]["fisrt"])

del(a["name"])
print(a)



