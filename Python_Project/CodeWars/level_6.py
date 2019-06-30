#Multiples of 3 or 5
def solution(number):
    return  sum([i if not i%5 else i if not i%3 else 0 for i in range(number)]) 

#Find the odd int
def find_it(seq):
    return list(filter(lambda x: x != None,[seq[i] if seq.count(seq[i]) % 2 else None  for i in range(len(seq))]))[0]

#Sum of Digits / Digital Root
def digital_root(n):
    return digital_root(sum([int(d) for d in str(n)])) if len(str(n)) > 1 else sum([int(d) for d in str(n)])

#Array.diff
def array_diff(a, b):
    return [item for item in a if item not in b]

#Bit Counting
def countBits(n):
    return str(bin(n)).count('1')
