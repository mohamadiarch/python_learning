# we have two kinds of set
# 1. set  2.frozen set

a={1,2,3}
a.add(3)
print(a)

a=frozenset({1,2,3})
print(a)

a=frozenset([1,2,3])
print(a)


# a.add(3)    # gets error
print(a)
print("frozen set are immutable")
