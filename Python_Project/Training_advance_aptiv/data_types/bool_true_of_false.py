a = bool(1) == True                   # True
b = bool(0) == False                  # True
c = True == True                         # True
d = True != False                        # True
e = bool(1) or 0                          # True
f = 1 and bool(0)                         # False
g = bool(bool("") == False) or False   # True
h = bool("False") is not bool(False)          # False

print(a)                                # True
print(b)                                # True
print(c)                                # True
print(d)                                # True
print(e)                                # True
print(f)                                # False
print(g)                                # True
print(h)                                # False