
a={"name":"mohammad","age":22}

l=[1,2,3]


n=454
print(a)
print(type(a))

print(a.get("name"))


print(a.get("father","no father"))
print(a)


a["name"]=a.get("mother"," no mother")
print(a)
