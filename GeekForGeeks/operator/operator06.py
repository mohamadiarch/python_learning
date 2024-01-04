a=10    # 1010
b=4      # 0100
# write bites under each other then calculate
# 1010
# 0100
# 0000 and
# 1110 or
print(bin(a))
print(bin(b))
print("-------------")
print(a&b)
print(a|b)
print(a^b)
print("------tilda-------")
print(~a)  # 1-0101 +0001 = 0110
print(~b)   # 1011 +0001 = 1100
print(bin(~a))
print(bin(~b))
# mokamel yek + 1 = mokamel do
# signed binary syetem ==> 1. one's complement 2. twos complement
print("-------------")
print(a<<b)
print(b>>a)
print("-------------")
print(a>>2)
print(a<<2)

