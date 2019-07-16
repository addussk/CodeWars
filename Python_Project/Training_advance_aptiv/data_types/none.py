a = None is None                                                                      # True
b = None is not None                                                                  # False
c = bool(bool(0) is not bool(None)) == False                                         # True
d = (bool(bool(1) is not bool(1)) == False and bool(None))                         # False
e = (bool(bool("Don't care") is not bool("Don't care")) == False and bool(True)) and (None is not None)   # False

print(a)    # True
print(b)    # False
print(c)    # True
print(d)    # False
print(e)    # False

