

# ternry
b= 1
a= 45 if b>5 
print(a)
# dota if posht ham

if a:=45> 20:
    print("jk w")


str = 45   # not errot
a= str(45)   # this get error

# tavabe asli ro mishe overwrite kard vali dge datsresi nadarim


a=[1,2,3,5]

b,*c=a   # unpackj
*b , c=a  
# tedad kamter ya bishter?
*_,a,b=[1,2,3,45]  # dummy variable 


a**2 for a in ls
ls2 = [i ** 2 for i in ls]
ls2 = [i for i in ls if i%2==0]




[1,2,3,45]   # age tedaad ziad bashe ram por mishe
# iter
it = iter(ls)   # ls az db mida
a= next(it)


a.sort()  # inplace
sorted(ls)
a.sort(reverse=true)


s={1,3,4,5,2}
s.add(2)
# set
s.union(s2)  # union means U ejtema
s.intersection(s2) # esht
s.difference(s2)  # -

s.remover(2)   # errot  if 2 not
s.discard(1)    # no error opp remove

try:
    s.remove(1)
except keyerror:
    print("gf")
execpt nameeror:
    print("sa")

a=(1)
a=(1,)   # tupple one item



a={a:45}
del a["name"]






import pprint  #(pretty print)  # print dict in terminal

dict.items()
dict.keys()
dcit.values()













