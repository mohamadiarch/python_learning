import os 
print(os.getcwd()) 

fh = open("./coursera_python_for_everyone/1.txt", "r")    # this is  a file handle
lines = fh.readlines() 
print(lines)    # WRAN: you can not read 
for line in lines:
    print(line)
    words = line.split()
    print(words , "this is words")
print(fh)



