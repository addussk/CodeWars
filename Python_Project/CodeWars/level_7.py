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

#Beginner Series #3 Sum of Numbers
def get_sum(a,b):
   return a if a == b else sum([number for number in range( a if a < b else b,(b if b > a else a) + 1 )])

#List Filtering
def filter_list(l):
   return list(filter(lambda element: isinstance(element,int) ,l))

# Disemvowel Trolls
def disemvowel(string):
    return "".join( letter for letter in string if letter.lower() not in "aeiou")

# Square Every Digit
def square_digits(num):
    return int("".join( str(pow) for pow in [ int(element)**2 for element in str(num) ]) )

# Jaden Casing Strings
def to_jaden_case(string):
    return " ".join( element.capitalize() for element in string.split() )

# Isograms
def is_isogram(string):
    if string != "":
        seen = set()
        arr = []
        for let in string:
            seen.add(let.lower())
            arr.append(let.lower())
        
        return len(arr) == len(seen)
    else: return True

# Sum of two lowest positive integers
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

# Growth of a Population
def nb_year(p0, percent, aug, p):
    sum, iter = p0, 0
    while(sum < p):
        iter += 1
        sum = sum + sum*(percent/100) + aug
        
    return iter 

# Credit Card Mask
def maskify(cc):
    print(len(cc))
    retVal = ""
    for idx in range(len(cc) - 4):
        retVal = retVal + '#'
    return retVal + cc[-4:]

# Is this a triangle?
def is_triangle(a, b, c):
    maks = max([a,b,c])
    rest = sum([a,b,c]) - maks
    return False if maks >= rest else True

# Find the next perfect square!
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    return -1 if not ((sq**(1/2)//1)**2 == sq) else (sq**(1/2) + 1)**2

# Two to One
def longest(s1, s2):
    seen = set()
    return "".join( let for let in sorted(s1 + s2) if let not in seen and not seen.add(let) )

# Regex validate PIN code
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

# Sum of odd numbers
def row_sum_odd_numbers(n):
    firstNum, x, retSum = 0, 2, []
    numElem = sum(range(n+1))

    if firstNum == 0:
        firstNum += 1
        retSum.append(1)

    while(firstNum < numElem):
        x += 1

        if x%2:
            firstNum += 1
            retSum.append(x)

    return sum(retSum[-n:])

# Binary Addition
def add_binary(a,b):
    return bin(a+b)[2:]

# Friend or Foe?
def friend(x):
    return [ name for name in x if len(name) == 4 ]

# Categorize New Member
def open_or_senior(data):
    return [ "Senior" if (member[0] >= 55 and member[1] > 7) else "Open" for member in data ]

# Ones and Zeros
def binary_array_to_number(arr):
    return int(("0b" + "".join(str(el) for el in arr)), 2)

# Find the divisors!
def divisors(integer):
    divisors = []
    for i in range(2,integer):
        if integer % i == 0:
            divisors.append(i)
            
    return divisors if divisors else "{} is prime".format(integer)

# Number of People in the Bus
def number(bus_stops):
    return sum([getIn[0] for getIn in bus_stops]) - sum([ getOff[1] for getOff in bus_stops ])

# String ends with?
def solution(string, ending):
    return ( string[:string.rfind(ending)] + ending ) == string

# Sum of the first nth term of Series
def series_sum(n):
    retArr = []
    if n == 0:
        return "0.00"
    if n < 2 :
        return "1.00"
    else:
        for elm in range(1,n*3,3):
            retArr.append((1 / elm))
        retVal = str(round(sum( retArr ),2 ))
        return retVal if len(retVal) == 4 else retVal + "0"