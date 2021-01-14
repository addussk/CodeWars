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

# Sort the Gift Code
def sort_gift_code(code):
    return "".join(sorted(code))

# Simple Fun #176: Reverse Letter
def reverse_letter(string):
    return "".join( let for let in string if (96 < ord(let) and 123 > ord(let)) )[::-1]

# Find the middle element
def gimme(input_array):
    return input_array.index(sorted(input_array)[1])

# Form The Minimum TAGS: #duplicates #sets
def min_value(digits):
    seen = set()
    return int("".join(sorted([ str(num) for num in digits if num not in seen and not seen.add(num) ])))

# Remove duplicate words #duplicates #sets #string
def remove_duplicate_words(s):
    seen = set()
    return " ".join([ el for el in s.split(' ') if el not in seen and not seen.add(el) ] )

# Sum of angles
def angle(n):
    return (n-2)*180

# Fizz Buzz
def fizzbuzz(n):
    return [ "FizzBuzz" if (not el%5 and not el%3) else  "Fizz" if not el%3 else "Buzz" if not el%5 else el for el in range(1,n+1) ] 

# Functional Addition
def add(n):
    '''Function that returns a function that adds n to any number'''
    def add2(k):
        return n + k
    return add2

# Round up to the next multiple of 5
def round_to_next5(n):
    return 0 if not n else (n//5)*5 if not n%5 else(n//5+1)*5

# Gauß needs help! (Sums of a lot of numbers).
def f(n):
    try:
        if n > 0:
            return sum(range(n+1))
        else: return None
    except:
        return None

# Building Strings From a Hash
def solution(pairs):
    return ",".join(sorted(([ "{} = {}".format(str(el), (pairs.get(el))) for el in pairs ])))

# Predict your age!
def predict_age(*argv):
    return ((sum([ el*el for el in argv]))**(1/2))//2

# Fix string case
def solve(s):
    return s.upper() if (len(s) - sum(map(str.islower, s))) > sum(map(str.islower, s)) else s.lower()

# Greet Me
def greet(name): 
    return "Hello {}!".format((name.lower()).capitalize())

def is_sorted_and_how(arr):
    return 'yes, ascending' if arr == sorted(arr) else 'yes, descending' if arr == sorted(arr, reverse=True) else 'no'

# Number Of Occurrences
def number_of_occurrences(element, sample):
    return sample.count(element)

# Power of two
def power_of_two(x):
    temp = 1
    while temp < x:
        temp = temp * 2
    return temp == x

# Most digits
def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))

# Flatten
def flatten(lst):
    arr = []
    for el in lst:
        if type(el) is list:
            arr.extend(el)
        else : arr.append(el)
    return arr 

# Basic Sequence Practice
def sum_of_n(n):
    size = n+1 if n>=0 else abs(n) + 1
    dir =(1 if n>=0 else -1)
    return [ (el * (el + 1) // 2) * dir  for el in range(size)]

# Thinkful - String Drills: Repeater
def repeater(string, n):
    return "".join( string for idx in range(n))

# Leap Years
def isLeapYear(year):
    return False if year % 4 or ( not year % 100 and year % 400) else True

# JavaScript Array Filter
def get_even_numbers(arr):
    return list(filter(lambda y: y%2 ==0 , arr))

# Flatten and sort an array #sort
def flatten_and_sort(array):
    arr = []
    for singleArray in array:
        arr.extend(singleArray)
    return sorted(arr)

# Boiled Eggs
def cooking_time(eggs):
    return 5*( eggs//8 + 1) if eggs%8 else 5*(eggs//8)

# Caffeine Script
def caffeine_buzz(n):
    return "{}{}".format("Coffee" if (not n%3 and not n%4) else "Java", "Script" if not n%2 else "" ) if ( not n%3 )  else "mocha_missing!"

# Row Weights
def row_weights(array):
    return (sum([ el for el,idx in zip(array, range(len(array))) if not idx%2] ) ,sum([ el for el,idx in zip(array, range(len(array))) if idx%2] ))

# Area of a Circle
import math
def circle_area(r):
    try:
        if r <= 0:
            return False
        else:
            return round(math.pi*(r**2),2)
    except:
        return False

# Elapsed Seconds
def elapsed_seconds(start, end):
    return (end - start).seconds

# # A Rule of Divisibility by 7
def seven(m):
    if not m :
        return (0,0)
    retVal, iter = (m//10) - 2* (m%10), 1
    while( retVal >= 100):
        iter += 1
        retVal = (retVal//10) - 2* (retVal%10)
    return (retVal, iter)

# Parts of a list
def partlist(arr):
    return [ (" ".join( arr[:(idx+1)]) , " ".join( arr[(idx+1):])) for idx in range(len(arr)-1) ]

# Refactored Greeting
class Person:
    def __init__(self, my_name):
        self.name = my_name
    
    def greet(my_name, your_name):
        return "Hello %s, my name is %s" % (your_name, my_name)
    
    def greet(self, your_name):
        return "Hello %s, my name is %s" % (your_name, self.name)

# Speed Control
import math
def gps(s, x):
    try:
        s = s/3600
        avrgSpeed = [ math.floor(((x[idx+1] - x[idx])/s )*10)/10 for idx in range(len(x)-1)]
        return max(avrgSpeed)
    except:
        return 0

# Greatest common divisor
def mygcd(x, y):    
    return max([i for i in range(1,min([x,y])+1) if (not x%i) and (not y%i)])

# Complete The Pattern #1
def pattern(n):
    return "" if not n else "\n".join([ ("{}".format(num))*num for num in range(1,n+1)])

# Sum of Triangular Numbers
def sum_triangular_numbers(n):
    return sum([ (el * (el + 1) // 2) for el in range(1, n+1) ]) if n > 0 else 0

# Alphabetical Addition
def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))

# Making Copies
def copy_list(l):
    return [ el for el in l]

#Find the nth Digit of a Number
def find_digit(num, nth):
    return -1 if nth <= 0 else 0 if nth>len(str(num)) else int(str(num)[-nth]) 

# Moves in squared strings (I)
def vert_mirror(strng):
    return "\n".join([el[::-1] for el in strng.split("\n")])

def hor_mirror(strng):
    return "\n".join(strng.split("\n")[::-1])

def oper(fct, s):
    return fct(s)    

# Return the Missing Element
def get_missing_element(seq): 
    i = 9
    while i in seq:
        i -= 1
    return i

# Alphabetical Addition
def add_letters(*letters):
    val = sum([ ord(let)-96 for let in letters ])
    return 'z' if not val%26 else chr( 96+ val%26)

# Love vs friendship
def words_to_marks(s):
    return sum([ ord(let)-96 for let in s])

# Digitize
def digitize(n):
    return [int(num) for num in str(n)]

# Simple beads count
def count_red_beads(n):
    return (n-1)*2 if n>0 else 0

# Sum of Minimums!
def sum_of_minimums(numbers):
    return sum([ min(row) for row in numbers ])

# Ordered Count of Characters
def ordered_count(inp):
    seen = set()
    return [ (el, inp.count(el)) for el in inp if el not in seen and not seen.add(el)]

# Averages of numbers
def averages(arr):
    return [ (arr[idx]+arr[idx+1])/2 for idx in range(len(arr)-1)] if arr else []

# Folding your way to the moon
def fold_to(distance):
    if distance < 0:
        return None
    thickness, iteration = 0.0001, 0
    while distance > thickness:
        thickness *= 2
        iteration +=1
    
    return iteration

# Simple Fun #74: Growing Plant
def growing_plant(upSpeed, downSpeed, desiredHeight):
    days, actualHeight = 0, 0
    while actualHeight < desiredHeight: 
        days += 1
        actualHeight += upSpeed
        
        if(actualHeight < desiredHeight):
            actualHeight -= downSpeed
        else: return days
    
    return 1

# Halving Sum
def halving_sum(n): 
    return sum([ n//(2**el) for el in range( int(n**(1/2)+1)) ])

# Regexp Basics - is it a vowel?
def is_vowel(s): 
    return s.lower() in "aeiou" if len(s) == 1 else False

# Maximum Product
def adjacent_element_product(arr):
    return max([ (arr[idx]*arr[idx+1]) for idx in range(len(arr)-1)])

# Arithmetic Sequence!
def nthterm(first, n, c):
    if n == 0: return first
    return nthterm(first, n - 1, c) + c

# Last
def last(*inp):
    try:
        return inp[-1][-1]
    except:
        return inp[-1]

# Find the vowels
def vowel_indices(word):
	return [ (idx+1) for idx in range(0, len(word)) if word[idx].lower() in "aeiouy" ]

# Substituting Variables Into Strings: Padded Numbers
def solution(value):
    return "Value is " + "0"*(5-len(str(value))) + str(value)

# Sum of array singles
def repeats(arr):
    return sum([ el for el in arr if arr.count(el) == 1])

# Currying functions: multiply all elements in an array
from inspect import signature
def curry(fnc):
    def inner(arg):
        if len(signature(fnc).parameters) == 1:
            return fnc(arg)

# Currying functions: multiply all elements in an array
def multiply_all(arr):
    def m(n):
        return [i*n for i in arr]
    return m

# Drying Potatoes
def potatoes(p0, w0, p1):
    return math.floor(w0 * (100 - p0) / (100 - p1))

# Sort Out The Men From Boys
def men_from_boys(arr):
    seen = set()
    return [ el for el in sorted(arr) if not el%2 and el not in seen and not seen.add(el)] + [ el for el in sorted(arr,reverse=True) if el%2 and el not in seen and not seen.add(el)]

# Make them bark!
def bark(self):
    return "Woof!"

Dog.bark = bark






