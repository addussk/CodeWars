input_val = input("Please enter value for converting:")


print(f'Meters: {int(input_val)}')                                    # int
print(f'Kilometers: {int(input_val)//1000}')                          # int
print(f'Miles: {float(input_val)/1608}')                               # float
print(f'Nautical Miles: {float(input_val)/1852}')                      # float