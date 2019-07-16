a = bool(False) #false
b = bool(True) #true

c = bool('a')   #true
d = bool('.')   #true
e = bool('0')   #true
f = bool('0.0') #true
g = bool('')    #false
h = bool(' ')   #true

i = bool(0) #false
j = bool(0.0)   #false
k = bool(-0)    #false
l = bool(-0.0+0.0j) #false
m = bool('-0.0+0.0j')   #true

n = bool(int('0'))  #false
o = bool(float('-0'))   #false\

print(h)