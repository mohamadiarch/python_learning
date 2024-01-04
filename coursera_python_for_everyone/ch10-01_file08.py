# List comprehension

b={"name":"ali","age":45,"country":"iran"}
# a= (v,k) for v,k in b.items()     -----error----- it should be list
a=[(k,v) for v,k in b.items()]
print(a)


# List comprehension creates a dynamic list
# List comprehension is a good way to reverse a tupple
