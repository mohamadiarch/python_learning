

a=10  #1010
b=4   #0100
print(a & b)
print(a| b)  #1110 =14 
print(~a)    #10 = 00001010 ==> toggle=11110101 ===> for reading to decimal ==> toggle again and plus to 1 
# print(!a)     #  we dont have !a , for not we use ~ tilde
print(a ^  b)   # this is XOR

# not is tilde but it does not negative a number ===> formula for tilde = -x-1 
print(-a)
