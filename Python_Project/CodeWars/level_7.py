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

# Dog.bark = bark

# Javascript filter - 1
def search_names(logins):
    return filter(lambda el: "_" in el[0], logins)

# Multiply characters
def spam(number):
    return 'hue' * number

# Factorial Factory
def factorial(n):
    if n <0: return None
    
    if n == 0: return 1
    return n * factorial(n-1)

# Sum of all arguments
def sum_args(*args):
    return sum(args)

# Basic Calculator
def calculate(x, op, y): 
    try:
        if op == "+":
            return x+y
        elif op == "-":
            return x-y
        elif op == "*":
            return x*y
        elif op == "/":
            return x/y
        else: return None
    except:
        return None

# Regexp Basics - is it a letter?
def is_letter(s):
    try:
        return ord(s.lower()) in range(96,122)
    except:
        return False

# Factorial
def factorial(n):
    if n <0: return None
    
    if n == 0: return 1
    return n * factorial(n-1)

# Find The Duplicated Number in a Consecutive Unsorted List
def find_dup(arr):    
    return [el for el in arr if arr.count(el) > 1 ][0]


# Complete The Pattern #2
def movie(card, ticket, perc):
    iter, totCostA, totCostB, ticketB = 2, ticket, card + ticket*perc, ticket*perc

    while math.ceil(totCostB) > totCostA:
        totCostA = ticket*iter
        ticketB = ticketB*perc
        totCostB = totCostB + ticketB
        if math.ceil(totCostB) < totCostA:
            return iter
        iter +=1
    return iter

# Collatz Conjecture Length
def collatz(n):
    l = 1
    while n > 1:
        l += 1
        if n % 2 == 0: n /= 2
        else: n = n * 3 + 1
    return l


# Smallest value of an array
def find_smallest(numbers,to_return):
    minVal = min(numbers)

    if to_return is "value":
        return minVal
    else:
        return numbers.index(minVal)

# Remove Duplicates
def unique(integers):
    seen = set()
    return [ el for el in integers if el not in seen and not seen.add(el)]

# Reverse a Number
def reverse_number(n):
    try:
        return int(str(n)[::-1])
    except:
        return -1*int(str(abs(n))[::-1])

# Vampire Numbers
def vampire_test(x, y):
    x, y, sum = str(x), str(y), str(x*y)
    return False if len(x) + len(y) != len(sum) else (min([ el in sum for el in x]) and min([g in sum for g in y]))

# Head, Tail, Init and Last
def head(arr):
    return arr[0]

def tail(arr):
    return arr[1:]

def init(arr):
    return arr[0:-1]

def last(arr):
    return arr[-1]

# Rotate for a Max
def max_rot(n):
    arr = []
    iter = len(str(n)) - 1
    for i in range(0,iter):
        arr.append(n)
        n = int( str(n)[:i] + str(n)[i+1:] + str(n)[i])
    return max(arr) if arr else 1


# Unlucky Days
def unlucky_days(year):
    return sum(date(year, month, 13).isoweekday() == 5 for month in range(1, 13))

# Unpacking Arguments
def spread(func, args):
    return func(*args)

# Sum of Odd Cubed Numbers
def cube_odd(arr):
    try:
        if list(filter(lambda x: isinstance(x, bool) ,arr)):
            return None
        else:
            arr = [el**3 for el in arr]
            return sum(filter(lambda x: x%2, arr))
    except: return None

# Counting power sets
def powers(lst):
    return 2**(len(lst))

# Complete The Pattern #2
def pattern(n):
    return "\n".join( [ "".join( [str(el) for el in range(n,x,-1)]) for x in range(n)] )

# Return the first M multiples of N
def multiples(m, n):
    return [i * n for i in range(1, m+1)]

# Milk and Cookies for Santa
def time_for_milk_and_cookies(dt):
    return dt.day == 24 and dt.month == 12

# Easy mathematical callback
def process_array(arr, callback):
    return list(map(callback, arr))

# Minimize Sum Of Array (Array Series #1)
def min_sum(arr):
    arr = sorted(arr)
    return sum([ arr[i]*arr[-i-1] for i in range(len(arr)//2) ])

# Number of Decimal Digits
def digits(n):
    return len(str(n))

# Alphabet war
def alphabet_war(fight):
    sumLeft = sum([ fight.count('w')*4, fight.count('p')*3, fight.count('b')*2, fight.count('s')*1 ])
    sumRight = sum([fight.count('m')*4,fight.count('q')*3,fight.count('d')*2,fight.count('z')*1])
    return "Let's fight again!" if sumLeft == sumRight else "Right side wins!" if sumRight > sumLeft else "Left side wins!"

# Limit string length - 1
def solution(st, limit): 
    return st if limit >= len(st) else st[:limit] + '.'*(3)

# shorter concat [reverse longer]
def shorter_reverse_longer(a,b):
    return b +a[::-1]+ b if len(a)>=len(b) else a +b[::-1]+ a 

# ToLeetSpeak
leetDict = {
  'A' : '@',
  'B' : '8',
  'C' : '(',
  'D' : 'D',
  'E' : '3',
  'F' : 'F',
  'G' : '6',
  'H' : '#',
  'I' : '!',
  'J' : 'J',
  'K' : 'K',
  'L' : '1',
  'M' : 'M',
  'N' : 'N',
  'O' : '0',
  'P' : 'P',
  'Q' : 'Q',
  'R' : 'R',
  'S' : '$',
  'T' : '7',
  'U' : 'U',
  'V' : 'V',
  'W' : 'W',
  'X' : 'X',
  'Y' : 'Y',
  'Z' : '2'
}

def to_leet_speak(str):
    return "".join( leetDict[el] if el != ' ' else ' ' for el in str)

# Alphabet symmetry
alphabet = {'a':1,
        'b':2,
        'c':3,
        'd':4,
        'e':5,
        'f':6,
        'g':7,
        'h':8,
        'i':9,
        'j':10,
        'k':11,
        'l':12,
        'm':13,
        'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
def solve(arr):
    return [ sum([ 1 for letter, pos in zip(el, range(len(el))) if alphabet[letter.lower()] == (pos+1) ]) for el in arr ]

# Coloured Triangles
dict = {
    "BG" : 'R',
    "GB" : 'R',
    "RG" : 'B',
    "GR" : 'B',
    "BR" : 'G',
    "RB" : 'G',
    "RR" : 'R',
    "GG" : 'G',
    "BB" : 'B',
}

def triangle(row):
    if row[0]*len(row) == row:
        return row[0]
    
    tmp, retRow, ln = "", row, len(row)-1

    while len(retRow)>2:
        for pos in range(0, ln):
            
            tmp = tmp + dict[retRow[pos:pos+2]]
        
        retRow = tmp
        tmp, ln = "", len(retRow)-1
    
    return dict[retRow]

# Small enough? - Beginner
def small_enough(array, limit):
    return  False if list(filter(lambda x: x > limit, array)) else True

# Birthday I - Cake
def cake(candles,debris):
    if not candles:
        return "That was close!"
    print(candles, debris)
    even = sum([ alphabet[debris[pos]] for pos in range(1,len(debris), 2) ])
    odd = sum([ ord(debris[pos]) for pos in range(0,len(debris), 2)])
    return 'That was close!' if candles*0.7 >= odd + even else 'Fire!'

# Automorphic Number (Special Numbers Series #6)
def automorphic(n):
    return "Automorphic" if str(n) == str(n**2)[-len(str(n)):] else "Not!!"

# Search for letters
def change(st):
	return "".join( '1' if chr(idx + 97) in st.lower() else '0' for idx in range(26) )

# Largest Elements
def largest(n,xs):
    return sorted(xs)[-n:]

# Simple Fun #152: Invite More Women?
def invite_more_women(arr):
    return arr.count(1) > arr.count(-1)

# Alternate case
def alternateCase(string):
    return string.swapcase()

# Monotone travel
def is_monotone(heights):
    return True if not heights else all(x<y for x, y in zip(heights, heights[1:])) or all(x<=y for x, y in zip(heights, heights[1:]))

# Array element parity
def solve(arr):
    return sum(set(arr))

# esreveR
def reverse(lst):
    out = list()
    for i in range(len(lst)-1,-1,-1):
        out.append(lst[i])
    return out

# Find Count of Most Frequent Item in an Array
def most_frequent_item_count(collection):
    try:
        seen = set(collection)
        return max( collection.count(el) for el in seen)
    except:
        return 0

# Word values
def name_value(my_list):
    return [ idx*sum( ord(let)-96 for let in s if ord(let)>96) for s,idx in zip(my_list, range(1, len(my_list) +1 )) ]

# Bumps in the Road
def bumps(road):
    return "Woohoo!" if road.count('n') < 16 else "Car Dead"    

# All unique
def has_unique_chars(string):
    seen = set()
    return "".join( el for el in string if el not in seen and not seen.add(el)) == string

# Sum even numbers
def sum_even_numbers(seq): 
    return sum(list(filter(lambda x: not x%2, seq)))   

# Looking for a benefactor
def new_avg(arr, newavg):
    futDon = (len(arr)+1) * newavg - sum(arr)
    if futDon >0:
        return math.ceil(futDon)
    else: raise 'ValueError'

# All Inclusive? #rotation
def contain_all_rots(n, in_arr):
    # Rotate for a Max
    arr = []
    iter = len(str(n))
    for i in range(0,iter):
        arr.append(n)
        n =  str(n)[1:] + str(n)[0]
    return all(( x in in_arr) for x in arr) if n else 1

# Indexed capitalization
def capitalize(s,ind):
    return "".join(list(map(lambda pos: s[pos].upper() if pos in ind else s[pos], range(len(s)))))

# Even numbers in an array
def even_numbers(arr,n):
    return list(filter(lambda x: not x%2, arr))[-n:]

# Disarium Number (Special Numbers Series #3)
def disarium_number(number):
    return "Disarium !!" if sum(list(map(lambda el,n : int(el)**n, str(number), range(1, len(str(number))+1 )))) == number else "Not !!"

# Product Of Maximums Of Array (Array Series #2)
from functools import reduce
def max_product(lst, n_largest_elements):
    arr = []
    while n_largest_elements:
        maxV = max(lst)
        arr.append(maxV)
        lst.remove(maxV)
        n_largest_elements -=1
    return reduce(lambda x, y : x*y, arr)

# Simple remove duplicates
def solve(arr): 
    seen = set()
    return [ el for el in arr [::-1] if el not in seen and not seen.add(el)][::-1]

# Simple consecutive pairs
def pairs(ar):
    print(ar)
    return  [ ar[pos] - 1 == ar[pos+1] or ar[pos] + 1 == ar[pos+1]  for pos in range(0, len(ar)-1, 2)].count(True)

# Building blocks
class Block():
    def __init__(self, ar):
        self.width = ar[0]
        self.leng = ar[1]
        self.height = ar[2]
    
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.leng

    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.height * self.leng * self.width
    
    def get_surface_area(self):
        return 2*self.height*self.leng + 2*self.width*self.height + 2*self.leng*self.width

# Build a square
def generate_shape(integer):
    return "\n".join( "+"*integer for row in range(integer))

# Return substring instance count
def solution(full_text, search_text):
    return full_text.count(search_text)

# By 3, or not by 3? That is the question . . .
def divisible_by_three(st): 
    return  sum( int(el) for el in st) in range(3, int(st)+1,3)

# STRONGN Strong Number (Special Numbers Series #2)
def strong_num(number):
    return "STRONG!!!!" if sum(  math.factorial(int(singleN)) for singleN in str(number)) == number else "Not Strong !!"

# max diff - easy
def max_diff(lst):
    try:
        return max(lst) - min(lst)
    except:
        return 0

# FIXME: Get Full Name
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        if  not self.first_name and not self.last_name:
            return ""
        elif self.first_name and not self.last_name:
            return self.first_name
        elif self.last_name and not self.first_name:
            return self.last_name
        else : return self.first_name + " " + self.last_name
    
# Nth power rules them all!
def modified_sum(a, n):
    return sum( el**n for el in a) - sum(a)

# My Languages #sorting #dict
def my_languages(results):
    results = sorted(results.items(), key = lambda x: x[1] , reverse=True)
    return [ el[0] for el in results if el[1] >= 60 ]

# Nth Smallest Element (Array Series #4)
def nth_smallest(arr, pos):
    for i in range(pos-1):
        arr.remove(min(arr))
    return min(arr)

# Say hello!
def greet(name):
    return "hello {}!".format(name) if name else None

# Tidy Number (Special Numbers Series #9)
def tidyNumber(n):
    return int("".join(sorted([ el for el in str(n)]))) == n

# Jumping Number (Special Numbers Series #4)
def jumping_number(number):
    try:
        stringN = str(number)
        lng = len(stringN) - 1
        return "Jumping!!" if not number//10 else "Jumping!!" if all([ abs(int(stringN[pos]) - int(stringN[pos+1]))==1 for pos in range(0, lng) ]) else "Not!!"
    except:
        return "Jumping!!"

# Float Precision
def solution(n):
    return round(n,2)












print(jumping_number(79))