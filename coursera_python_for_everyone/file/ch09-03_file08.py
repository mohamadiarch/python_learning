


fh= open("./coursera_python_for_everyone/1.txt", "r")
for line in fh:
    a=line.rstrip()
    print(a)
    wlist= a.split()
    for word in wlist:
        print(word)
        for letter in word:
            print(letter)

a= 11111112323243443989
for n in str(a):
    print(n)
