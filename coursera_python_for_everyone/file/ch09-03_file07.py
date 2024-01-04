

fh= open("./coursera_python_for_everyone/1.txt", "r")
print(fh)
for line in fh:
    # print(line , type(line)) 
    a=line.rstrip()
   # print(a)
    print(line)


 # rstrip  is  a method  of string 
 # rstrip do  not print anything
 # rstip return a new string
  # split is another method for strings 
  # ------------split-------rstrip---- 
  # ----------read-----------readlines
