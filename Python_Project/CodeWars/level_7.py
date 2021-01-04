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

# Remove the minimum
def remove_smallest(numbers):
    copyArr = [ el for el in numbers]
    try:
        copyArr.pop(copyArr.index(min(copyArr)))

        return copyArr
    except:
        return []

# Reverse words
def reverse_words(text):
    return " ".join([ el[::-1] for el in text.split(' ')])

# Odd or Even?
def odd_or_even(arr):
    return "odd" if sum(arr)%2 else "even"

# Breaking chocolate problem
def break_chocolate(n, m):
    if n+m:
        return n*m -1
    else: return 0

# The highest profit wins!
def min_max(lst):
    return [min(lst), max(lst)]

# Money, Money, Money
def calculate_years(principal, interest, tax, desired):
    currentVal = principal
    cnt = 0
    while currentVal < desired:
        currentVal = currentVal + currentVal*(interest) - currentVal*(interest)*tax
        cnt += 1
    return cnt

# Find the stray number
def stray(arr):
    setAr = set()
    for el in arr:
        setAr.add(el)
    
    for el in setAr:
        if arr.count(el) == 1:
            return el

# Don't give me five!
def dont_give_me_five(start,end):
    return len([ el for el in range(start,end+1) if '5' not in str(el)])

# Largest 5 digit number in a series
def solution(digits):
    return max([ int( digits[ startIdx:(startIdx+5)] ) for startIdx in range(len(digits) - 4 )])

# Triangular Treasure TAGS: #overflow #datatypes
def triangular(n):
    return n * (n + 1) // 2 if n > 0 else 0

# Factorial TAGS: #exceptions
import math
def factorial(n):
    if n >= 0 and n <= 12:
        return math.factorial(n)
    else: raise ValueError


# Sum of a sequence
def sequence_sum(start, end, step):
    return sum(range(start, end+1, step))

# Make a function that does arithmetic TAGS: #calculator
def arithmetic(a, b, operator):
    if operator == 'add':
        return a+b
    elif operator == 'subtract':
        return a-b
    elif operator == 'multiply':
        return a*b
    elif operator == 'divide':
        return a/b
    else:
        return "error"

# Count the Digit TAGS: #string
def nb_dig(n, d):
    return sum([ str(sqNum**2).count(str(d) ) for sqNum in range(n+1) ])

# Summing a number's digits
def sum_digits(number):
    return sum( [ int(digNum) for digNum in str(abs(number))] )

# Count the divisors of a number
def divisors(n):
    cnt = 0
    for idx in range(1, (n+1)):
        if not n%idx:
            cnt += 1
    return cnt

# No oddities here
def no_odds(values):
    return [ num for num in values if not num%2 ]

# Sort Numbers
def solution(nums):
    return [] if not nums else sorted(nums)

# Anagram Detection TAGS: #ANAGRAM
def is_anagram(test, original):
    arr1 = [ ord(let.lower()) for let in test ]
    arr2 = [ ord(let.lower()) for let in original ]
    return sum(arr1) == sum(arr2)

# Sum of all the multiples of 3 or 5
def find(n):
    return sum( [ num for num in range(n+1) if (not num%3 or not num%5)] )

# Two Oldest Ages
def two_oldest_ages(ages):
    maxValue = max(ages)
    ages.remove(maxValue)
    secMaxValue = max(ages)
    return [ secMaxValue, maxValue ]

# Maximum Length Difference
def mxdiflg(a1, a2):
    try:
        print([ len(el) for el in a1 ], [ len(el) for el in a2 ])
        lenVal1 = {"min": min([ len(el) for el in a1 ]), "max": max([ len(el) for el in a1 ]) }
        lenVal2 =  {"min": min([ len(el) for el in a2 ]), "max": max([ len(el) for el in a2 ]) }
        
        return max([ abs(lenVal1["max"] - lenVal2["min"]), abs(lenVal2["max"] - lenVal1["min"]) ]) if a1 and a2 else -1
    except:
        return -1

# Testing 1-2-3
def number(lines):
    return [ str(el) +": "+ let for el, let in zip(range(1, 1+len(lines)), lines) ] 

# Remove anchor from URL
def remove_url_anchor(url):
    return url[:url.find('#')] if '#' in url else url

# Find the capitals
def capitals(word):
    arrPos = []
    for let, position in zip(word, range(len(word))):
        if 64 < ord(let) and ord(let) < 91:
            arrPos.append(position)
    return arrPos

# Deodorant Evaporator
def evaporator(content, evap_per_day, threshold):
    days = 0
    limitVal = (content * (threshold/100) )
    while content > limitVal:
        days += 1
        content = content - (content * (evap_per_day/100) )

    return days 

# Two fighters, one winner.
def declare_winner(fighter1, fighter2, first_attacker):
    while fighter1.health > 0 and fighter2.health > 0:
        if first_attacker == fighter1.name:
            fighter2.health -= fighter1.damage_per_attack
            
            if fighter2.health <= 0:
                return fighter1.name
            else : 
                fighter1.health -= fighter2.damage_per_attack
                if fighter1.health <= 0:
                    return fighter2.name
                
        else : 
            fighter1.health -= fighter2.damage_per_attack
            
            if fighter1.health <= 0:
                return fighter2.name
            else : 
                fighter2.health -= fighter1.damage_per_attack
                if fighter2.health <= 0:
                    return fighter1.name

# Sort array by string length TAGS #sort
def sort_by_length(arr):
    dic = {}
    for el in arr:
        dic[el] = len(el)
    return [ string[0] for string in sorted(dic.items(), key=lambda element: element[1])]

# Are the numbers in order?
def in_asc_order(arr):
    return arr == sorted(arr)

# The Coupon Code
import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    current_date = current_date.replace(',', '')
    expiration_date = expiration_date.replace(',', '')
    cur = current_date.split(' ')
    expir = expiration_date.split(' ')

    date_time_cur = datetime.datetime.strptime(((cur[0])[:3] +' '+ cur[1] +' '+ cur[2] ), '%b %d %Y')
    date_time_exp= datetime.datetime.strptime(((expir[0])[:3] +' '+ expir[1] +' '+ expir[2] ), '%b %d %Y')
    
    return entered_code is correct_code and int(date_time_cur.strftime('%Y%m%d')) <= int(date_time_exp.strftime('%Y%m%d'))

# Maximum Multiple
def max_multiple(divisor, bound):
    return max([ i for i in range(bound + 1) if not i % divisor ]) 

# Alternate capitalization TAGS: #string
def capitalize(s):
    return ["".join(let.lower()  if pos%2 else let.upper() for let, pos in zip(s, range(len(s))) ), "".join(let.upper()  if pos%2 else let.lower() for let, pos in zip(s, range(len(s))) ) ]
        
# Sum of numbers from 0 to N
def show_sequence(n):
    return "+".join( str(num) for num in range(n+1)) +" = {}".format(sum(range(n+1))) if n > 0 else str(n) +'<0' if n != 0 else "0=0"

# Palindrome chain length TAGS: #palindrome
def palindrome_chain_length(n):
    iter, temp = 0, 0
    while str(n) != str(n)[::-1]:
        iter += 1
        n = n + int(str(n)[::-1])
        
    return iter

print(sort_by_length(["beg123213", "to", "beg", "life"]))