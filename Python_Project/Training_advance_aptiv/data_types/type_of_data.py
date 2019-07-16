value = 1_000_00

print(type(value))

value = 10.
value1 = .44
value2 = 1e6
value3 = -1e6
value4 = 1e-4

print(f'{value}  {value1} {value2}  {value3}  {value4}')

import sys

#min and max value of float
print(f'{sys.float_info.min} {sys.float_info.max}')

#infinity representation
print(float('-inf'))

#precission
pi = 3.14159265359

round(pi, 2)
round(pi, 3)
