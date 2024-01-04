# we have two memory in python 1. stack memory 2.heap mempry

# stack
"""
numbers + boolean + chars   => fixed memory size
for Lists the reference is stored on the stack, the actual data (the list elements in this case) is stored on the heap.
because the ref(address) has a fixed size.
method calls are stored on the stack
# methods are execuyed from stack memory
"""


#### heap
"""
objects and data structuers and non-primitive data types  => dynamic memory allocation
list + dict + objs 
When an object is created in Python, it is allocated on the heap, and a
reference to that object is stored on the stack.
 
"""

"""
stack memory:
----------
|f1():   |          
|      z |   
|      a |   
----------

----------
|main:   |
|     x  |
|     y  |  
|        |
----------

# main
x=12
y=16
def f1():
    a=45
    z=78
# when we say a=45, 45 is an integer object and a is a reference to that object
"""
a=[12,3]
b=[12,3]
c=a
print(a is c)
print(a is b)


a.append(111)
print(a)
print(c)

