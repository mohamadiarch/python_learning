import os 
print(os.getcwd()) 

fh = open("./coursera_python_for_everyone/1.txt", "r")    # this is  a file handle
lines = fh.readlines()       # readlines  make a list 
print(lines)    
print("------------------------")
for line in lines:
    print(line)
    print("---------line------------")
    words = line.split()
    print(words , "this is words")
print(fh)



