#task 1 - iq test

def iq_test(string):
    number = string.split()
    noOdds = 0
    noEven = 0
    position = 0

    for i in range (0,len(number)):
        if(int(number[i])%2 ==0):
            noEven = noEven + 1
        else:
            noOdds = noOdds + 1

    if(noOdds>noEven):
        for i in range(0, len(number)):
            if( int( number[i]) % 2 == 0):
                position = i +1
    if (noEven > noOdds):
        for i in range(0, len(number)):
            if (int(number[i]) % 2 != 0):
                position = i + 1
    return position

#task 2 - shortest word

def find_short(phrase):
    x = phrase.split()
    len_shortest_word = int(x[0].__len__())

    for i in range(0, int(x.__len__())):
        if int(x[i].__len__()) < len_shortest_word :
            len_shortest_word = int(x[i].__len__())

    return len_shortest_word #shortest word length

#similar solution

def find_short2(s):
    return min(len(x) for x in s.split(" "))


# DNA to RNA Conversion
def DNAtoRNA(dna):
    string1 = ""
    for letter in dna:
        if letter == 'T':
             string1 += "U"
        else :
            string1 += letter
    return string1
def DNAtoRNA2(dna):
    return "".join(["U" if c=="T" else c for c in dna])

# Grasshopper - Summation
def summation(num):
    return sum(range(1,num+1))

#Function 1 - hello world
def greet():
    return "hello world!"

#The Feast of Many Beasts
def feast(beast, dish):
    return  (beast[0] == dish [0] and beast[-1] == dish [-1])

#L1: Set Alarm
def set_alarm(employed, vacation):
    return (not vacation and employed)

#Are You Playing Banjo?
def areYouPlayingBanjo(name):
    # if name[0].lower() == 'r':
    #     ending = " plays banjo"  
    # else :
    #     ending = " does not play banjo"
    return (name + " plays banjo") if name[0].lower() == 'r' else (name + " does not play banjo")
#print(areYouPlayingBanjo("Mikke"))

#Capitalization and Mutability
def capitalizeWord(word):
    return  word[0].upper() + word[1:].lower()

def printer_error(s):
    
    len_string = len(s)
    #print(len_string)
    licznik = 0
    tablica = ['n','o','p','q','r','s','t','u','w','y','x','z'] 
    for i in s:
        if i in tablica :
            licznik = licznik + 1

    x = "%s/%s" % (licznik,len_string)
    print(x)
    licznik = 0

def song_decoder(song):
    song = song.split('WUB')
    original_version = []
    for i in song:
        if i != '':
            original_version += [i]
    return ' '.join(original_version)
                                
def spin_words(sentence):
    sentence = sentence.split(' ')
    for i in sentence:
        if (len(i)>5):
            zmienna = sentence.index(i)
            sentence[zmienna] = i[::-1]
    return ' '.join(sentence)
 
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def find_missing_letter(chars): 
    tab  = []
    i = 0
    j = 0
    print(len(alfabet))
    for i in range(len(chars)):
        tab.append(chars[i].lower())

    count = alfabet.index(chars[0].lower())
    counter=0 
    result = 0

    for j in range(count,26,1):
        if tab[0:counter] == alfabet[count:j]:
            counter+=1
            result = j
    if chars[0] == chars[0].upper():
        return alfabet[result].upper()
    else:
        return alfabet[result]
 
dictionary = {
    'a' : "1",
    'b' : "2",
    'c' : "3",
    'd' : "4",
    'e' : "5",
    'f' : "6",
    'g' : "7",
    'h' : "8",
    'i' : "9",
    'j' : "10",
    'k' : "11",
    'l' : "12",
    'm' : "13",
    'n' : "14",
    'o' : "15",
    'p' : "16",
    'q' : "17",
    'r' : "18",
    's' : "19",
    't' : "20",
    'u' : "21",
    'v' : "22",
    'w' : "23",
    'x' : "24",
    'y' : "25",
    'z' : "26"

}

def alphabet_position(text):
    orginal_string = []
    for i in text:
        if i.lower() in dictionary:
            orginal_string.append(dictionary.get(i.lower()))
    return ' '.join(orginal_string)

def high(text):
    array_words = text.split(' ')
    
    result = 0
    for i in array_words:
        value_word = 0
        for j in i:
            value_word += int(dictionary.get(j))
        if(value_word > result):
            result = value_word
            output = i
    return output

# def high(x):
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
# print(high('man i need a taxi up to ubud'))

def bouncingBall(h = 0.0, bounce = 0.0, window = 1.5):
    if h >0 and 0< bounce <1 and window <h:
        times = 0
        while h>window:
            if h > window:
                times +=1
            h = h*bounce
            if h > window:
                times +=1
        return times
    else: return -1


def to_weird_case(string):
    
    list_string = []
  
    for word in string.split(' '):
        counter = 0
        word_return = ""
        for letter in word:
            if counter % 2: #even
               word_return +=  letter.lower()  
            else:       #odd
                word_return +=  letter.upper()
            counter +=1
        list_string.append(word_return)
    return ' '.join(list_string)

def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))
    
# def to_weird_case(string):
#     return " ".join(to_weird_case_word(str) for str in string.split())  
#print(to_weird_case('This is a test'))

def create_phone_number(n):
    index = 0
    i = 0
    string = ""
    char_list = ['(',') ','-']

    for number in n:
        if((index == 0) or  (index == 3) or (index == 6)) :
            string += char_list[i]
            i+=1

        string += (str(number))
        index +=1
    
    return string 
# def create_phone_number(n):
#   return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


#Abbreviate a Two Word Name
def abbrevName(name):
    string1, string2  =   name.split(" ")
    return (string1[0] +   "." +   string2[0]).upper()
    # x   =    "".join(c if c.isupper() else "" for c in name)
    # return x[0] +   "." +   x[1]
#print(abbrevName("Sam Harris"))

#Even or Odd
def even_or_odd(number):
    return "Odd" if number%2 else "Even"
#print(even_or_odd(2))

#Find the smallest integer in the array
def find_smallest_int(arr):
    arr.sort()
    return arr[0]
#print(find_smallest_int([78, 56, 232, 12, 11, 43]))

#String repeat
def repeat_str(repeat, string):
    return "".join(string for i in range(repeat)) 
#print(repeat_str(4, 'a'))

#Return Negative
def make_negative( number ):
    return (number - 2*number) if number >=  0 else number
#print(make_negative(42))

#Sum of positive
def positive_sum(arr):
    wynik = 0
    for i in arr:
        if i >= 0:
            wynik = wynik   +   i
        else:  continue
    return wynik
#print(positive_sum([1,2,3,4,5]))

#Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#Convert a Number to a String!
def number_to_string(num):
    return str(num)

#Remove First and Last Character
def remove_char(s):
    return s[1:-1]
#print(remove_char('eloquent'))

#Counting sheep...
array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ]

def count_sheeps(arrayOfSheeps):
    result = 0

    for i in arrayOfSheeps:
        if i == True:
            result = result + 1
        else : continue
    return result
#other solution return arrayOfSheeps.count(True)
#print(count_sheeps(array1))

#Reversed Strings
def solution(string):
    return ''.join(reversed(string))

#Jenny's secret message
def greet2(name):
  if name == "Johnny":
        return "Hello, my love!"
  return "Hello, {name}!".format(name=name)

#Basic Mathematical Operations
def basic_op(operator, value1, value2):
    if operator == '+':
        result  =   value1 + value2 
    elif operator == '-':
        result  =   value1 - value2 
    elif operator == '*':
        result  =   value1 * value2 
    elif operator == '/':
        result  =   value1 / value2 
    return result
    #other resolution
    # def basic_op(operator, value1, value2):
    # return eval("{}{}{}".format(value1, operator, value2))
    # def basic_op(o, a, b):
    # return {'+':a+b,'-':a-b,'*':a*b,'/':a/b}.get(o)
#print(basic_op('+', 4, 7))

#Square(n) Sum
def square_sum(numbers):
    return sum(i * i for i in numbers)

#print(square_sum([1,2]))

#A Needle in the Haystack
def find_needle(haystack):
    return "found the needle at position {}".format(haystack.index("needle"))
#print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 2/12/2019

#Convert number to reversed array of digits
def digitize(n):

    return list(map(int,(list(reversed(str(n))))))

#print(digitize(35231))

#Convert a String to a Number!
def string_to_number(s):
    return int(s)

#Count of positives / sum of negatives
def count_positives_sum_negatives(arr):
    return [] if ((arr == [])) else [len(list(filter(lambda x: x > 0,arr))),sum(filter(lambda x: x < 0,arr))]

#print(count_positives_sum_negatives([]))

#Calculate average
def find_average(array):
    return 0 if len(array) == 0 else (sum(array)/len(array))
#other solution
    # try:
    #     return sum(array) / len(array)
    # except ZeroDivisionError:
    #     return 0
#print(find_average([ 1, 2, 3 ]))

#Invert values
def invert(lst):
    return [] if lst == [] else list(map(lambda x: x*(-1),lst))

#Sum without highest and lowest number
def sum_array(arr):
    return 0 if (arr == None or len(arr)<3) else sum(arr) - min(arr) - max(arr)

#print(sum_array([ 3, 5]))
from functools import reduce
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 02/13/2019
#Find Maximum and Minimum Values of a List
def min(arr):
    arr.sort()
    return arr[0]

def max(arr):
    arr.sort()
    return arr[len(arr)-1]
import math
#Century From Year
def century(year):
    return math.ceil(year/100)

#print(century(1700))

#You Can't Code Under Pressure #1
def double_integer(i):
    return i**2

#Do I get a bonus?
def bonus_time(salary, bonus):
    return "${}".format(salary *10) if bonus else "${}".format(salary)

#Sentence Smash
def smash(words):
    return " ".join(words)

#print(smash(["hello", "world"]))

#Volume of a Cuboid
def getVolumeOfCubiod(length, width, height):
    return length*width*height

#Double Char
def double_char(s):
    return "".join(list(map(lambda x: x + x,s)))

#print(double_char("String")) # SSttrriinngg")

#Transportation on vacation
def rental_car_cost(d):
    if d > 6:
        return (d*40 -50)
    elif 3<= d < 8:
        return (d*40 -20)
    else:
        return d*40
 
#Function 3 - multiplying two numbers
def multiply(arg1,arg2):
     return arg1*arg2

#Reversed Words
def reverseWords(str):#function which convert every word in string to an element of a list then reverses order in list then  each element of list merge to one string 
    return " ".join(reversed(str.split())) 

#print(reverseWords("hello world!"))

#Convert a Boolean to a String
def boolean_to_string(b):
    return "True" if b else "False"

#Rock Paper Scissors!
def rps(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"

#Count by X
def count_by(x, n):
    wynik = 0
    lst = []
    for i in range(n):
        wynik = wynik + x
        lst.append(wynik)
    return lst 

#print(count_by(1, 5))

#Sum Arrays  
def sum_array_vol2(a):
    return 0 if a == [] else sum(a)

#Fake Binary
def fake_bin(x):
    return ''.join("0" if int(i) <5 else '1' for i in str(x))

#print(fake_bin(45385593107843568))

#Reversed sequence
def reverse_seq(n):
    return [i for i in range(n,0,-1)] 

#print(reverse_seq(5))

#Unfinished Loop - Bug Fixing #1
def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i = i+1
    return res

#Is n divisible by x and y?
def is_divisible(n,x,y):
    return True if n % x == 0 and  n % y == 0 else False

#print(is_divisible(48,3,4))

#Opposites Attract
def lovefunc( flower1, flower2 ):
    return True if ((even_or_odd(flower1) == "Odd" and even_or_odd(flower2) == "Even") or (even_or_odd(flower2) == "Odd" and even_or_odd(flower1) == "Even")) else False

#print(lovefunc(1,3))

#Beginner - Lost Without a Map
def maps(a):
    return list(map(lambda x: x*2,a))

#Short Long Short
def solution_vol2(a, b):
    return "{}".format(a)  + b + "{}".format(a) if len(b) > len(a) else "{}".format(b)  + a + "{}".format(b)
#A function within a function
def always(n = 0):
    def multiplier():
        return  n
    return multiplier

# three = always(3)
# print(three())

#altERnaTIng cAsE <=> ALTerNAtiNG CaSe
def to_alternating_case(string):
    return ''.join( letter.upper() if letter.islower() else letter.lower() for letter in string)

#print(to_alternating_case("HeLLo WoRLD"))

#Stringy Strings
def stringy(size):
    return ''.join('1' if not i%2 else '0' for i in range(size))

#MakeUpperCase
def make_upper_case(s):
    return ''.join( chr(ord(letter) - 32) if ord(letter) in range(97,123) else letter for letter in s)
# for sweep case return ''.join((chr(ord(letter)+32) if ord(letter) in range(65,90) else chr(ord(letter) - 32)) if(ord(letter) in range(65,90) or ord(letter) in range(97,122)) else letter for letter in s)

#How many lightsabers do you own?
def howManyLightsabersDoYouOwn(s = "Nobody"):
    return 18 if s == "Zach" else 0

#Regular Ball Super Ball
class Ball(object):
    # ball_type = "regular" 
    def __init__(self,type_ball = "regular"):
        self.ball_type = type_ball

#Get the mean of an array
def get_average(marks):
    return math.floor(sum(marks)/(len(marks)))
#print(get_average([2, 2, 2, 2]))

number_to_name_string = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
}
#Switch it Up!
def switch_it_up(number):
    return number_to_name_string[number]
#print(switch_it_up(0))

#You only need one - Beginner
def check(seq, elem):
    return elem in seq
    #return True if [True if elem == element else False for element in seq].count(True) else False

#Function 2 - squaring an argument
def square(n):
    return n*n

#Keep up the hoop
def hoop_count(n):
    return "Great, now move on to tricks" if n>10 else "Keep at it until you get it"

#Sleigh Authentication
class Sleigh(object):
    name = 'Santa Claus'
    password = 'Ho Ho Ho!'
    def authenticate(self, name, password):
        return True if (self.name == name and self.password == password) else False

# sleigh = Sleigh()
# print(sleigh.name)

# print(sleigh.authenticate('Santa Claus', 'Ho Ho!'))

#Basic variable assignment
a = "code"
b = "wa.rs"
name = a + b

#Simple multiplication
def simple_multiplication(number) :
    return number* 9 if number%2 else number*8

#My head is at the wrong end!
def fix_the_meerkat(arr):
    return list(reversed(arr))

#Correct the mistakes of the character recognition software
def correct(string):
    dic = {
        '0':'O',
        '1':'I',
        '5':'S',
    }
    return ''.join( letter if letter not in dic else dic[letter] for letter in string)
#other instresting solution
#   return string.translate(str.maketrans("501", "SOI"))
#   return string.replace('1','I').replace('0','O').replace('5','S')
#print(correct("L0ND0N"))

#I love you, a little , a lot, passionately ... not at all
def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1] 

#Count the Monkeys!
def monkey_count(n):
    return range(1,n+1)

#Beginner - Reduce but Grow
def grow(arr):
    return reduce(lambda x,y: x*y,arr)

#Returning Strings
def greet_vol3(name):
    return "Hello, {} how are you doing today?".format(name)

#Calculate BMI
def bmi(weight, height):
    bmi = weight / height **2
    if bmi <=18.5:
        return  "Underweight"
    elif bmi <=25:
        return  "Normal"
    elif bmi <= 30 :
        return "Overweight"
    else : return "Obese"

#Basic Training: Add item to an Array
#websites.append("codewars")

#Exclusive "or" (xor) Logical Operator
def xor(a,b):
    return True if a^b else False

#Number toString
a = str(123)

#Color Ghost
import random
colors = ['yellow', 'purple', 'red', 'white']
class Ghost(object):
    def __init__(self):
        self.color = colors[random.randrange(0,4)]

#How good are you really?
def better_than_average(class_points, your_points):
    return True if sum(class_points)/len(class_points) < your_points else False

#Plural
def plural(n):
    return "Plural for {}".format(n) if n != 1 else "1 is singular!"

#The 'if' function
def _if(bool, func1, func2):
    return func1() if bool else func2()

#Is he gonna survive?
def hero(bullets, dragons):
    return True if bullets//dragons >= 2 else False 

#Kata Example Twist
websites = []

for i in range(0,1000):
    websites.append("codewars")

#Convert a string to an array
def string_to_array(s):
    return s.split(" ")

#Reversing Words in a String
def reverse(st):
    return ' '.join(list(reversed(st.split())))

#print(reverse("Hello World!"))

#If you can't sleep, just count sheep!!
def count_sheep(n):
    return ''.join("{} sheep...".format(i) for i in range(1,n+1))

#Third Angle of a Triangle
def other_angle(a, b):
    return 180 - a - b

#Thinkful - Logic Drills: Traffic light
def update_light(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

language_dic = {
'english': 'Welcome',
'czech': 'Vitejte',
'danish': 'Velkomst',
'dutch': 'Welkom',
'estonian': 'Tere tulemast',
'finnish': 'Tervetuloa',
'flemish': 'Welgekomen',
'french': 'Bienvenue',
'german': 'Willkommen',
'irish': 'Failte',
'italian': 'Benvenuto',
'latvian': 'Gaidits',
'lithuanian': 'Laukiamas',
'polish': 'Witamy',
'spanish': 'Bienvenido',
'swedish': 'Valkommen',
'welsh': 'Croeso'
}
#Welcome!
def greet_vol4(language):
    return language_dic[language] if language in language_dic  else 'Welcome'

#Dollars and Cents
def format_money(amount):
    return "${:.2f}".format(float(amount))

#Thinkful - Number Drills: Pixelart planning
def is_divisible_vol2(wall_length, pixel_size):
    return True if not wall_length % pixel_size else False

#Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    catYears = [15,24,(24 + 4*(human_years-2))]
    dogYears = [15,24,(24 + 5*(human_years-2))]
    x = int(not human_years == 1) + int(human_years > 2)
    return [human_years,catYears[ x ],dogYears[ x ]]

#Find numbers which are divisible by given number
def divisible_by(numbers, divisor):
    return list(filter(lambda number : number != -1 , [i if i% divisor == 0 else -1 for i in numbers]))

#Will there be enough space?
def enough(cap, on, wait):
    return 0 if cap >= (on+wait) else (on+wait)-cap

#Sum Mixed Array
def sum_mix(arr):
    return sum(int(number_to_int) for number_to_int in arr)

#Filter out the geese
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    return list(filter(lambda word_in_geese_arr : word_in_geese_arr not in geese, birds))

#Array plus array
def array_plus_array(arr1,arr2):
    return sum(arr1) + sum(arr2)

#Twice as old
def twice_as_old(dad_years_old, son_years_old):
    return  2*son_years_old - dad_years_old if 2*son_years_old > dad_years_old else  dad_years_old - 2*son_years_old

#Is this my tail?
def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    if sub == tail:
        return True
    else:
        return False

#Get Planet Name By ID
def get_planet_name(id):
    switch = {
        1:"Mercury",
        2:"Venus",
        3:"Earth",
        4:"Mars",
        5:"Jupiter",
        6:"Saturn",
        7:"Uranus",
        8:"Neptune",
    }
    return switch[id]

#Vowel remover
vowel_tab = ['a', 'e', 'i', 'o', 'u','y']
def shortcut( inputStr ):
     return "".join(letter for letter in inputStr if letter not in vowel_tab)

#Sort and Star
def two_sort(array):
     
    return "".join(letter + "***" for letter in sorted(array)[0])[:-3]

# print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])) #'b***i***t***c***o***i***n' )

#Is the string uppercase?
def is_uppercase(inp):
    return True if inp.isupper() else False

#Training JS #7: if..else and ternary operator
def sale_hotdogs(n):
    return 100*n if n < 5 else 95*n if n<10 else n*90 

#All Star Code Challenge #18
def str_count(string , letter):
    return 0 if len(string) < 1 else string.count(letter)

#Hex to Decimal
def hex_to_dec(s):
    return  int(s,16)

#Beginner Series #2 Clock
def past(h, m, s):
    return s*1000 + m*60*1000  + h*60*60*1000

#Surface Area and Volume of a Box
def get_size(w,h,d):
    return [2*(w*h+w*d+d*h),w*h*d]

#Grasshopper - Terminal game combat function
def combat(health, damage):
    return 0 if health - damage < 0 else health - damage

#Grasshopper -  book
GRADE = {
    100: 'A',
    90 : 'A',
    80 : 'B',
    70 : 'C',
    60 : 'D',
}

def get_grade(s1,s2,s3):
    print(int(((s1+s2+s3)/3)/10)*10)
    return 'F' if int(((s1+s2+s3)/3)/10)*10 not in GRADE else  GRADE[int(((s1+s2+s3)/3)/10)*10]

# print(get_grade(70, 55, 100))
GRADE_VOL2 = {
    1: 'A',
    0.9 : 'A',
    0.8 : 'B',
    0.7 : 'C',
    0.6 : 'D',
}
#Grader
def grader(score):
    return 'F' if not 0.6 <= score <= 1 else GRADE_VOL2[int(score*10)/10]

import math

#Beginner Series #4 Cockroach
def cockroach_speed(s):
    return math.floor(s*1000/36)

#repeatIt
def repeat_it(string,n):
    return "Not a string" if not isinstance(string,str) else "".join(string for i in range(0,n))

# print(repeat_it("Not a string", 3))

#Add Length
# def add_length(string):
#     return element + str(len(element))for element in string.split()
#
# print(add_length('apple ban'))

#Grasshopper - Debug
#from __future__ import division

def weather_info(temp):
    c = convertToCelsius(temp)
    if (c > 0):
        return (str(c) + " is above freezing temperature")
    else:
        return (str(c) + " is freezing temperature")


def convertToCelsius(temperature):
    celsius = (temperature - 32) * (5 / 9)
    return celsius

#Watermelon
def divide(weight):
    return True if  weight > 2 and not weight % 2 else False

#Return to Sanity
def mystery():
    results = {
        'sanity': 'Hello'
    }
    return results

#Duck Duck Goose
def duck_duck_goose(players, goose):
    return players[(goose % len(players) -1)].name

#Lario and Muigi Pipe Problem
def pipe_fix(array):
    return [element for element in range(min(array), max(array) + 1)]

# Squash the bugs
def find_longest(string):
    spl = string.split(" ")
    longest = 0

    for i in range(0, len(spl)):
        if (spl[i].__len__() > longest): longest = spl[i].__len__()

    return longest

#String Templates - Bug Fixing #5
def build_string(*args):
    return "I like {}!".format(", ".join(args))

#Find out whether the shape is a cube
def cube_checker(volume, side):
    return False if ((volume <= 0  or side <= 0) or (side**3 != volume )) else True

#Pre-FizzBuzz Workout #1
def pre_fizz(n):
    return [ i for i in range(1,n+1)]

#Loading Kata: Remove duplicates from list
def distinct(seq):
    return sorted(set(seq), key = seq.index)

thisset = {"apple", "banana", "apple", "cherry"}

thisset.update(["orange", "mango", "grapes", "apple"])

#Beginner Series #1 School Paperwork
def paperwork(n, m):
    return n*m if (n> 0 and m > 0) else 0

#How many stairs will Suzuki climb in 20 years?
sunday = [6737, 7244, 5776, 9826, 7057, 9247, 5842, 5484, 6543, 5153, 6832, 8274,
          7148, 6152, 5940, 8040, 9174, 7555, 7682, 5252, 8793, 8837, 7320, 8478, 6063,
          5751, 9716, 5085, 7315, 7859, 6628, 5425, 6331, 7097, 6249, 8381, 5936, 8496,
          6934, 8347, 7036, 6421, 6510, 5821, 8602, 5312, 7836, 8032, 9871, 5990, 6309, 7825]

monday = [9175, 7883, 7596, 8635, 9274, 9675, 5603, 6863, 6442, 9500, 7468, 9719,
          6648, 8180, 7944, 5190, 6209, 7175, 5984, 9737, 5548, 6803, 9254, 5932, 7360, 9221,
          5702, 5252, 7041, 7287, 5185, 9139, 7187, 8855, 9310, 9105, 9769, 9679, 7842,
          7466, 7321, 6785, 8770, 8108, 7985, 5186, 9021, 9098, 6099, 5828, 7217, 9387]

tuesday = [8646, 6945, 6364, 9563, 5627, 5068, 9157, 9439, 5681, 8674, 6379, 8292,
           7552, 5370, 7579, 9851, 8520, 5881, 7138, 7890, 6016, 5630, 5985, 9758, 8415, 7313,
           7761, 9853, 7937, 9268, 7888, 6589, 9366, 9867, 5093, 6684, 8793, 8116, 8493,
           5265, 5815, 7191, 9515, 7825, 9508, 6878, 7180, 8756, 5717, 7555, 9447, 7703]

wednesday = [6353, 9605, 5464, 9752, 9915, 7446, 9419, 6520, 7438, 6512, 7102,
             5047, 6601, 8303, 9118, 5093, 8463, 7116, 7378, 9738, 9998, 7125, 6445, 6031, 8710,
             5182, 9142, 9415, 9710, 7342, 9425, 7927, 9030, 7742, 8394, 9652, 5783, 7698,
             9492, 6973, 6531, 7698, 8994, 8058, 6406, 5738, 7500, 8357, 7378, 9598, 5405, 9493]

thursday = [6149, 6439, 9899, 5897, 8589, 7627, 6348, 9625, 9490, 5502, 5723, 8197,
            9866, 6609, 6308, 7163, 9726, 7222, 7549, 6203, 5876, 8836, 6442, 6752, 8695, 8402,
            9638, 9925, 5508, 8636, 5226, 9941, 8936, 5047, 6445, 8063, 6083, 7383, 7548, 5066,
            7107, 6911, 9302, 5202, 7487, 5593, 8620, 8858, 5360, 6638, 8012, 8701]

friday = [5000, 5642, 9143, 7731, 8477, 8000, 7411, 8813, 8288, 5637, 6244, 6589, 6362,
         6200, 6781, 8371, 7082, 5348, 8842, 9513, 5896, 6628, 8164, 8473, 5663, 9501,
         9177, 8384, 8229, 8781, 9160, 6955, 9407, 7443, 8934, 8072, 8942, 6859, 5617,
         5078, 8910, 6732, 9848, 8951, 9407, 6699, 9842, 7455, 8720, 5725, 6960, 5127]

saturday = [5448, 8041, 6573, 8104, 6208, 5912, 7927, 8909, 7000, 5059, 6412, 6354, 8943,
            5460, 9979, 5379, 8501, 6831, 7022, 7575, 5828, 5354, 5115, 9625, 7795, 7003,
            5524, 9870, 6591, 8616, 5163, 6656, 8150, 8826, 6875, 5242, 9585, 9649, 9838,
            7150, 6567, 8524, 7613, 7809, 5562, 7799, 7179, 5184, 7960, 9455, 5633, 9085]

stairs = [sunday,monday,tuesday,wednesday,thursday,friday,saturday]

def stairs_in_20(stairs):
    sum_all = 0
    for element in stairs:
        sum_all += sum(element)

    return 20*sum_all

# print(stairs_in_20(stairs))

#Grasshopper - Debug sayHello
def say_hello(name):
    return "Hello, {}".format(name)

#How old will I be in 2099?
list_string = ["You are {} year{} old.", "You were born this very year!","You will be born in {} year{}."]

def calculate_age(year_of_birth, current_year):
    resolution = year_of_birth - current_year
    return list_string[0].format(resolution*(-1),'s') if resolution < (-1) else  list_string[0].format(resolution*(-1),"") if resolution == -1 else list_string[1] if resolution == 0 else list_string[2].format(resolution,"") if resolution == 1 else list_string[2].format(resolution,"s")

#Drink about
list_of_drink = ["drink toddy","drink coke","drink beer","drink whisky"]

def people_with_age_drink(age):
    return list_of_drink[(age > 13) + (age > 17) + (age >= 21) ]

#Bin to Decimal
def bin_to_decimal(inp):
    return int(inp,2)

#Enumerable Magic #3 - Does My List Include This?
def include(arr,item):
    return True if arr.count(item) else False

#String cleaning
def string_clean(s):
    number = "0123456789"
    return "".join(element if element not in number else "" for element in s)

#get character from ASCII Value
def get_char(c):
    return chr(c)

dict_num_weekday = {
    1 : "Sunday",
    2 : "Monday",
    3 : "Tuesday",
    4 : "Wednesday",
    5 : "Thursday",
    6 : "Friday",
    7 : "Saturday"
}
#Return the day
def whatday(num):
    return "Wrong, please enter a number between 1 and 7" if num not in range(1,8)  else dict_num_weekday[num]

#Grasshopper - Messi goals function
def goals(*argv):
    return sum(argv)

#101 Dalmatians - squash the bugs, not the dogs!
def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
  
    respond = dogs[0] if n <= 10 else dogs[1] if n <= 50  else dogs[3] if n ==101 else dogs[2]

    return respond

#Grasshopper - Terminal game move function
def move(position, roll):
    return position + 2*roll

#Swap Values
def swap_values(args): 
    args[0], args[1] = args[1], args[0]
    
    return args

#Well of Ideas - Easy Version
def well(x):
    return 'Fail!' if 'good' not in x else 'Publish!' if x.count('good') in range(1,3) else 'I smell a series!'

#import numpy 
#Difference of Volumes of Cuboids
# def find_difference(a, b):
#     return abs(numpy.prod(a) - numpy.prod(b))
# todo: resolve problem with importing module

#5 without numbers !!
def unusual_five():
    return len("asdfg")

#A Strange Trip to the Market
def is_lock_ness_monster(string):
    return False if ( ("tree fiddy" not in string) and ("3.50" not in string) and ("three fifty" not in string) ) else True

#Remove First and Last Character Part Two
def array(string):
    if len(string) < 5:
        return None
    
    else:
        x = string[1:-1].replace(',',"")
        return x[1:-1]

#print(array('1,3,3'))
import math
def nearest_sq(n):
    if math.ceil(math.sqrt(n))**2 == n:
        return n
    
    else:
        x1 = math.floor(math.sqrt(n))
        x2 = math.ceil(math.sqrt(n))
        
        return math.pow(x1,2) if abs(math.pow(x1,2) - n) < abs(math.pow(x2,2) - n)  else math.pow(x2,2)
 
#Check the exam
def check_exam(arr1,arr2):
    score = 0
    for mergedElem in list(zip(arr1, arr2)):
        score += 4 if mergedElem[0] == mergedElem[1] else 0 if mergedElem[0] == "" or mergedElem[1] == "" else -1

    return 0 if score <= 0 else score

#For UFC Fans (Total Beginners): Conor McGregor vs George Saint Pierre
texArr = ["I am not impressed by your performance.", "I'd like to take this chance to apologize.. To absolutely NOBODY!"]

def quote(fighter):
    print(fighter.lower())
    return texArr[0] if fighter.lower() == 'george saint pierre' else texArr[1]

#Student's Final Grade
def final_grade(exam, projects):
    if exam >90 or projects >10:
        return 100# final grade
    elif exam >75 and projects >=5:
        return 90# final grade
    elif exam >50 and projects >=2:
        return 75# final grade
    elif exam <50 or projects <2 :
        return 0# final grade
    else:
        return 0

#noobCode 01: SUPERSIZE ME.... or rather, this integer!
def super_size(num):
    array = list(map(int, str(num)))
    array.sort( reverse = True)
    return int("".join([str(i) for i in array]))

import numpy
#Expressions Matter
def expression_matter(*argv):
    return max([ (list(argv)[0] * sum(list(argv)[1:])), numpy.prod(list(argv)), (list(argv)[0] + numpy.prod(list(argv)[1:])), sum(list(argv)[:2] * list(argv)[2]), sum(list(argv)) ] )

#Find the first non-consecutive number
def first_non_consecutive(arr):
    for element in arr[1:]:
        if element - 1 not in arr:
            return element

#Basic subclasses - Adam and Eve
class Human:
    def _init_(self):
        pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    adam = Man()
    eve = Woman()
    return [adam,eve]

#Palindrome Strings
def is_palindrome(string):
    covertedToString = str(string) 
    return False if False in [True if covertedToString[pos] == covertedToString[-1-pos] else False for pos in range(int(len(covertedToString)/2))] else True

#Area or Perimeter
def area_or_perimeter(l , w):
    return l*l if l == w else 2*w + 2*l

#No zeros for heros
def no_boring_zeros(n):
    while(1):
        if n % 10:
            break
        n = n / 10
        
    return int(n)

#Hello, Name or World!
def hello(name = None):
    return "Hello, World!" if name is None else "Hello, World!" if len(name) < 1 else  "Hello, {}!".format("".join([name[0].upper(), name[1:].lower()]))

#Simple validation of a username with regex
def validate_usr(username):
    retVal = False
    if 3 < len(username) < 17:
        for element in username:
            if ord(element) == 95 or (ord(element) < 123 and 95 < ord(element)) or ( 47 < ord(element) < 58):
                retVal = True
            else: 
                retVal = False
                break
                
    return retVal

#To square(root) or not to square(root)
def square_or_square_root(arr):
    return [int(element**(1/2)) if ((element**(1/2))*element)%element == 0 else element**2 for element in arr]
    
#Filling an array (part 1)
def arr(n = 0): 
    return [number for number in range(n)] if n > 0 else []

#Printing Array elements with Comma delimiters
def print_array(arr):
    return ",".join([str(element) for element in arr])

#The falling speed of petals
def sakura_fall(v):
    return  400/v if v >0 else 0

#Triple Trouble
def triple_trouble(one, two, three):
    return "".join("".join(a) for a in zip(one, two, three))
    # return "".join(one[i] + two [i] + three[i] for i in range(len(one)))

#What's the real floor?
def get_real_floor(n):
    return n if n < 0 else 0 if n in [0,1] else n - 1 if n < 13 else n - 2
    
#Find the Difference in Age between Oldest and Youngest Family Members
def difference_in_ages(ages):
    return ( min(ages), max(ages), max(ages) - min(ages))

#Grasshopper - Function syntax debugging
def main(verb, noun):
    return verb + noun

#A wolf in sheep's clothing
def warn_the_sheep(queue):
    return 'Pls go away and stop eating my sheep' if 0 == (queue.index('wolf') + 1 - len(queue)) else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.__len__() - queue.index('wolf') - 1)

#Grasshopper - Messi Goals
la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals

#Is it even?
def is_even(n): 
    return True if not n%2 else False

#Removing Elements
def remove_every_other(my_list):
    array = []
    index = 0
    for parametr in my_list:
        if not index % 2:
            array.append(parametr)
        index += 1
    return array

#N-th Power
def index(array, n):
    return -1 if n >= len(array) else array[n]**n


#Grasshopper - Check for factor
def check_for_factor(base, factor):
    return True if base // factor == base / factor else False

# Remove duplicates from list
def dup_distinct(seq):
    cloneArray = []
    for elem in seq:
        if elem not in cloneArray:
            cloneArray.append(elem)
    return cloneArray

#Smallest unused ID
def next_id(arr):
    for idx in range(0, len(arr)):
        if idx not in arr:
            break
        if arr[-1] == idx:
            idx +=1

    return idx

#L1: Bartender, drinks!
drinks_dic = {
    "jabroni": "Patron Tequila",
    "school counselor": "Anything with Alcohol",
    "programmer":"Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
    "anything else": "Beer"
}
def get_drink_by_profession(param):
    return drinks_dic['anything else'] if param.lower() not in drinks_dic else  drinks_dic[param.lower()]

#Subtract the sum
def subtract_sum(number):
    return "apple"

# The Wide-Mouthed frog!
def mouth_size(animal): 
  return "small" if animal.lower() == "alligator" else "wide"

# Remove First and Last Character Part Two
def array(strng):
    return ' '.join(strng.split(',')[1:-1]) or None

# Find Multiples of a Number
def find_multiples(integer, limit):
    return  [ x for x in range( integer, limit+1, integer)]

# Tip Calculator
tip_dic = {
    "terrible":  0,
    "poor":  0.05,
    "good":  0.1,
    "great":  0.15,
    "excellent":  0.2,
}

def calculate_tip(amount, rating):
    return 'Rating not recognised' if rating.lower() not in tip_dic else math.ceil(amount * tip_dic[rating.lower()])  

# Enumerable Magic #25 - Take the First N Elements
def take(arr,n):
    return arr[:n]

# Quarter of the year
def quarter_of(month):
    return 1 if month < 4 else 2 if month < 7 else 3 if month < 10 else 4

# Thinkful - Number Drills: Blue and red marbles
def guess_blue(blue_start, red_start, blue_pulled, red_pulled):
    return (blue_start - blue_pulled) / ( (red_start - red_pulled) + (blue_start - blue_pulled) )

# Classic Hello World
class Solution:
    
    def main(*args):
        print("Hello World!")
        pass

# SpeedCode #2 - Array Madness
def array_madness(a,b):
    return True if sum( [ (lambda x: x**2)(x) for x in a ] )  > sum( [ (lambda c: c**3)(c) for c in b ] ) else False

# What is between?
def between(a,b):
    return [x for x in range(a,b+1)]

# Add Length
def add_length(str_):
    return [x+" "+ str(len(x)) for x in str_.split(" ")]

#Palindrome Strings
def is_palindrome(string):
    covertedToString = string.lower() 
    return False if False in [True if covertedToString[pos] == covertedToString[-1-pos] else False for pos in range(int(len(covertedToString)/2))] else True

# Barking mad
class Dog ():
    def __init__(self, breed):
        self.breed = breed
    def bark(self):
        return "Woof"  
    
    

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")

# Super Duper Easy
def problem(a):
    try:
        input = int(a)
        return a*50 +6
    except ValueError:
        try:
            input = float(a)
            return a*50 +6
        except ValueError:
            return "Error"

# Grasshopper - Array Mean
def find_average(nums):
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0

# Parse float
def parse_float(string):
    try:
        return float(string)
    except:
        return None

# Multiple of index
def multiple_of_index(l):
    return [l[i] for i in range(1, len(l)) if l[i] % i == 0]

# Holiday VI - Shark Pontoon
def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if ((pontoon_distance / you_speed) >= (shark_distance / (shark_speed / (2 if dolphin  else 1)))):
        return 'Shark Bait!'
    else:
        return 'Alive!'

# Alan Partridge II - Apple Turnover
def apple(x):
    return "It's hotter than the sun!!" if int(x)**2 > 1000 else "Help yourself to a honeycomb Yorkie for the glovebox."

# How do I compare numbers?
def what_is(x):
    if x == 42:
        return 'everything'
    elif x == (42**2) :
        return 'everything squared'
    else:
        return 'nothing'

# Multiplication table for number
def multi_table(number):
    return "".join( "{} * {} = {}\n".format(el,number,str(el*number))  for el in range(1,10) ) + "{} * {} = {}".format(10,number,str(10*number))

# Closest elevator
def elevator(left, right, call):
    return "right" if ( abs(right-call) <= abs(left-call) ) else "left"

# Leonardo Dicaprio and Oscars
def leo(oscar):
    return "Leo finally won the oscar! Leo is happy" if oscar == 88 else "Not even for Wolf of wallstreet?!" if oscar == 86 else "Leo got one already!" if oscar > 88 else "When will you give Leo an Oscar?"

# get ascii value of character
def get_ascii(c):
    return ord(c)

# Take the Derivative
def derive(coefficient, exponent): 
    return "{}x^{}".format((coefficient * exponent),(exponent - 1))

# Sum The Strings
def sum_str(a, b):
    return "0" if not a and not b else a if not b else b if not a else  str(int(a) + int(b))

# Is it a number?
def isDigit(string):
    for remChar in ['.']:
        string = string.replace(remChar,"")
    
    try:
        val = int(string)
        return True
    except ValueError:
        return False

# No Loops 2 - You only need one
def check(a, x): 
    return True if x in a else False

# Area of a Square
def square_area(A):
    return round((((A*4)/(2*math.pi))**2),2)

# simple calculator
def calculator(x,y,op):
    try:
        if op == "+":
            return int(x)+int(y)
        elif op == "-":
            return int(x)-int(y)
        elif op == "*":
            return int(x)*int(y)
        elif op == "/":
            return int(x)/int(y)
        else: return "unknown value"
    except:
        return "unknown value"

# validate code with simple regex
def validate_code(code):
    return str(code).startswith(('1','2','3'))

# Who is going to pay for the wall?
def who_is_paying(name):
    return [name, name[:2]] if len(name) > 2 else [name]

# Remove the time
def shorten_to_date(long_date):
    return long_date.split(',')[0]

# Object Oriented Piracy
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        return True if (self.draft - self.crew*1.5 ) > 20 else False

# Find the Integral
def integrate(coefficient, exponent):
    return "{}x^{}".format(( coefficient // (1 + exponent)),(exponent + 1))

# Sum of Multiples
def sum_mul(n, m):
    try:
        if( n > 0 and m > 0 ):
            return sum([num for num in range(n,m,n)])
        else: return "INVALID"
    except:
        return "INVALID"

# 8kyu interpreters: HQ9+
LINES = "{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall."
SONG = '\n'.join( LINES.format("{} bottles".format(n), "{} bottle".format(n-1)+"s"*(n!=2)) for n in range(99,1,-1) )
SONG += """
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""

def HQ9(code):
    return {'H': 'Hello World!', 'Q': 'Q', '9': SONG}.get(code, None)

# Find the Slope
def find_slope(points):
    try:
        return str((points[3] - points[1]) // (points[2] - points[0]))
    except:
        return "undefined"

# Find the position!
def position(alphabet):
    return "Position of alphabet: {}".format(dictionary[alphabet])

# Fix the Bugs (Syntax) - My First Kata
def my_first_kata(a,b):
    try:
        if(type(a) is int and type(b) is int):
            return a % b + b % a
        else: return False
    except:
        return False

# Incorrect division method
def divide_numbers(x,y):
    return x / y

# Exclamation marks series #2: Remove all exclamation marks from the end of sentence
def remove(s):
    temp_arr =  s[::-1]
    counter = 0
    for el in temp_arr:
        if el == "!":
            counter -=1
        else: break
    return s[:counter] if counter else s

# FIXME: Replace all dots
import re
def replace_dots(s):
    return re.sub(r"\.", "-", s)

# Switch/Case - Bug Fixing #6
def eval_object(v):
    return {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }.get(v['operation'],1)

# Online RPG: player to qualifying stage?
def playerRankUp(pts):
     return False if pts < 100 else "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up."

# Merge two sorted arrays into one
def merge_arrays(arr1, arr2):
    seen = set()
    return [x for x in sorted(arr1 + arr2) if x not in seen and not seen.add(x)]
  
# Classy Classes
class Person:
    def __init__(self,name,age):
        self.info="{}s age is {}".format(name,age)

# Man in the west
def check_the_bucket(bucket):
    return True if "gold" in bucket else False

# Wilson primes
def am_i_wilson(n):
    return True if n in (5,13,563) else False

# Classy Extensions
class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "{} meows.".format(self.name)

# Evil or Odious
def evil(n):
    return "It's Odious!" if bin(n)[2:].count("1") % 2 else "It's Evil!"

# Is there a vowel in there?
def is_vow(inp):
    return [ chr(el) if el in (97, 101, 105, 111, 117) else el for el in inp  ]

# Grasshopper - Variable Assignment Debug
a = "dev"
b = "Lab"

name = a + b

# Polish alphabet
dic_polish_letter = {
    'ą' : 'a',
    'ć' : 'c',
    'ę' : 'e',
    'ł' : 'l',
    'ń' : 'n',
    'ó' : 'o',
    'ś' : 's',
    'ź' : 'z',
    'ż' : 'z',
}
def correct_polish_letters(st): 
    return "".join([el if el not in ('ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż') else  dic_polish_letter[el] for el in st ])

# Price of Mangoes
def mango(quantity, price):
    return quantity * price - quantity // 3 * price

# Finish Guess the Number Game
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
    
    def guess(self,n):
        try:
            if self.lives > 0:
                if n == self.number:
                    return True
                else: 
                    self.lives -= 1
                    return False
            else:
                    raise ValueError('Expect error: "Omae wa mo shindeiru"')
        except ValueError as ve:
            raise Error(ve)

# Who ate the cookie?
def cookie(x):
    try:
        len(x)
        return "Who ate the last cookie? It was Zach!"
    except:
        if x == True or x == False:
            return "Who ate the last cookie? It was the dog!"
        return "Who ate the last cookie? It was Monica!"

# Get number from string
def get_number_from_string(string):
    return int("".join( [el for el in string if ord(el) < 58 and ord(el) > 47] ) )

# Pillars
def pillars(num_pill, dist, width):
    return (num_pill - 1) * dist * 100 + (num_pill - 2)*width if num_pill > 1 else 0

# Character Frequency
def char_freq(message):
    dic = {}
    for el in message:
        dic[el] = message.count(el)
    return dic

# Grasshopper - Create the rooms
rooms = {
  'firstRoom': {
    'name': 'Saw I',
    'description': 'Easy level',
    'completed': True,
  },
  'secondRoom': {
    'name': 'Saw II',
    'description': 'Medium level',
    'completed': False,
  },
  'thirdRoom': {
    'name': 'Saw III',
    'description': 'Hardcore level',
    'completed': None,
  }
}

# Unexpected parsing
def get_status(is_busy):
    if is_busy:
        status = "busy"  
    else: 
        status = "available"
    return { 'status': status}

# Chuck Norris VII - True or False? (Beginner)
def ifChuckSaysSo():
    return bool(0)

# Fuel Calculator
def fuel_price(litres, price_per_litre):
    if litres >= 10:
        disc = 0.25
    elif litres >= 8:
        disc = 0.20
    elif litres >= 6:
        disc = 0.15
    elif litres >= 4:
        disc = 0.1
    elif litres >= 2:
        disc = 0.5
    else: disc = 0
    return litres * ( price_per_litre - disc) 

# What's wrong with these identifiers?
Person = {
  '1stname': "John",
  'second-name': "Doe",
  'email@ddress': "john.doe@email.com",
  'male.female': "M"
}

# Fix your code before the garden dies!
def rain_amount(mm):
    if (mm < 40):
         return "You need to give your plant " + str(40 - mm) + "mm of water"
    else:
         return "Your plant has had more than enough water for today!"

# Draw stairs
def draw_stairs(n):
    return ("".join("".join(" " for e in range(i)) + "I\n" for i in range(n) ))[:-1]

# Gravity Flip
def flip(d, a):
    return sorted(a) if d == 'R' else sorted(a)[::-1]

# Grasshopper - Terminal Game Turn Function
def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

# NBA full 48 minutes average
def nba_extrap(ppg, mpg):
    return 0 if not mpg else round((ppg * (48/mpg)), 1)

# Multiply the number
def multiply(n):
    return pow(5,len(str(abs(n))))*n

# Localize The Barycenter of a Triangle
def bar_triang(pointA, pointB, pointC): # points A, B and C will never be aligned
    # your code here
    return [ round((pointA[0] + pointB[0] + pointC[0])/3, 4), round((pointA[1] + pointB[1] + pointC[1])/3, 4)] # coordinates of the barycenter expressed up to four decimals
                    # (rounded result)

# Collatz Conjecture (3n+1)
def hotpo(n):
    iter = 0
    while n != 1:
        if n % 2 :
            n = 3*n + 1  
        else:
            n = n / 2
        iter += 1
        
    return iter


# Logical calculator
def logical_calc(array, op):
    if op == 'AND':
        return False if False in array else True
    if op == 'OR':
        return True if True in array else False
    if op == 'XOR':
        return True if array.count(True) % 2 else False
    
# Heads and Legs
def animals(heads, legs):
    return (0,0) if (heads == 0 and legs == 0) else "No solutions" if (heads <= 0 or legs <= 0) else ( (heads - (0.5*legs - heads)) , (0.5* legs - heads) ) if ( (round(legs/2 - heads) == (legs/2 - heads) ) and (heads - (0.5*legs - heads) >= 0 ) and ((0.5* legs - heads) >= 0 )) else "No solutions"

# Coefficients of the Quadratic Equation
def quadratic(x1, x2):
    return (1, -1*(x1 + x2), x1*x2)

# What's up next?
def next_item(xs, item):
    try:
        x = None
        while (1):
            xs = iter(xs)
            x = next(xs, None)
            if x == None:
                break
            elif x == item:
                return next(xs)
        return next(xs, None)
    except:
        return None
    

# Grasshopper - Bug Squashing
health = 100
position = 0
coins = 0

def main():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

# BASIC: Making Six Toast.
def six_toast(num):
    return abs(6 - num)

# Compare within margin
def close_compare(a, b, margin = 0):
    return 0 if margin >= abs(a-b) else -1 if a < b else 1 if b < a else 0

# Grasshopper - Terminal Game #1
class Hero(object):
    def __init__(self, name = 'Hero', pos = '00', hp = 100, dmg = 5, exp = 0):
        self.name = name
        self.position = pos
        self.health = hp
        self.damage = dmg
        self.experience = exp
        pass

# Age Range Compatibility Equation
import math
def dating_range(age):
    return "{}-{}".format(math.floor(age/2+7), (age - 7)*2 ) if age >= 14 else "{}-{}".format(math.floor(age - 0.1 * age), math.floor(age + 0.1 * age) )

# Count the number of cubes with paint on
def count_squares(cuts):
    return pow(cuts+1,3) - pow(cuts-1,3)

# Pirates!! Are the Cannons ready!??
def cannons_ready(gunners):
    return 'Fire!' if 'nay' not in [gunners.get(el) for el in gunners] else 'Shiver me timbers!'




print(next_item(iter(range(1, 20)), 12))