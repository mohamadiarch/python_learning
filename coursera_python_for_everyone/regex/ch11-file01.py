
import re
a= "From: ali@gmail.com, From: mamad@gmail.com"
b= re.findall("\S+@\S+",a)
c= re.search("\S+@\S+45",a)
print(b)
print(c)

if(c):
    print("true")
else:
    print("false")

# re.findall create a list
# re.search returns obj or None 
# we can use re.serach inside if 
