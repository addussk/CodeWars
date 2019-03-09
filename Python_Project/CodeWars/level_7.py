import math

#Vowel Count
def getCount(inputStr):
    vowel_str = 'aeiouAEIOU'
    num_vowels = 0
    return len([x for x in inputStr if x in vowel_str])

#Get the Middle Character
def get_middle(s):
    return s[(len(s)//2-1):len(s)//2+1 ] if not len(s)%2 else s[len(s)/2]

#Mumbling
def accum(s):
   # return '-'.join(s.capitalize() for s in  [s[i]*(i+1) for i in range(len(s))])
    return '-'.join(c.upper() + c.lower() * i for i,c in enumerate(s))
   
#You're a square!
def is_square(n):    
    return True if (int(n**(1/2)))**2 == n else False

#Highest and Lowest
def high_and_low(numbers):
    return  str(max([int(element) for element in numbers.split(" ")])) + " " + str(min([int(element) for element in numbers.split(" ")]))

#Complementary DNA
def DNA_strand(dna):
   return dna.translate(str.maketrans("ATCG", "TAGC"))

#Exes and Ohs
def xo(s):
    return True if s.lower().count('x') == s.lower().count('o') else False

#Descending Order   
def Descending_Order(num):
   return int(''.join(sorted(str(num),reverse = True)))

