#Multiples of 3 or 5
def solution(number):
    return  sum([i if not i%5 else i if not i%3 else 0 for i in range(number)]) 

#Find the odd int
def find_it(seq):
    return list(filter(lambda x: x != None,[seq[i] if seq.count(seq[i]) % 2 else None  for i in range(len(seq))]))[0]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))