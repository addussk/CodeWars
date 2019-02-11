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

# print()

# print(find_short("bitcoin take over the world maybe who knows perhaps"))
# print(find_short("turns out random test cases are easier than writing out basic ones"))
# print(find_short("lets talk about javascript the best language"))
# print(find_short("i want to travel the world writing code one day"))
# print(find_short("Lets all go on holiday somewhere very cold"))

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
#print(DNAtoRNA2("TTAAGCT"))

# Grasshopper - Summation

def summation(num):
    return sum(range(1,num+1))

#print(summation(8))

#Function 1 - hello world
def greet():
    return "hello world!"
#print(greet())

#The Feast of Many Beasts
def feast(beast, dish):
    return  (beast[0] == dish [0] and beast[-1] == dish [-1])
    
# print(feast("chickadee", "chocolate cake"))
# print(feast("brown bear", "bear claw"))

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
#print(capitalizeWord("LLmawzaxm"))

def printer_error(s):
    
    len_string = len(s)
    #print(len_string)
    licznik = 0
    tablica = ['n','o','p','q','r','s','t','u','w','y','x','z'] 
    for i in s:
        if i in tablica :
            licznik = licznik + 1
    
    #print(licznik)

    x = "%s/%s" % (licznik,len_string)
    print(x)
    licznik = 0
#string = "addsadasdnasjda"
# printer_error(string)


def song_decoder(song):
    song = song.split('WUB')
    original_version = []
    for i in song:
        if i != '':
            original_version += [i]
    return ' '.join(original_version)

# print(song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"))
                                
def spin_words(sentence):
    sentence = sentence.split(' ')
    for i in sentence:
        if (len(i)>5):
            zmienna = sentence.index(i)
            sentence[zmienna] = i[::-1]
    return ' '.join(sentence)
    
# print(spin_words("Hey fellow warriors")
 

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
    
    
# lista = ['a','b','c','d','f']
# lista2 = ['O','Q','R','S']
# print(find_missing_letter(['O','Q','R','S']))

 
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
#print(alphabet_position("The narwhal bacons at midnight."))

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

# print(bouncingBall(30, 0.66, 1.5))

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

#print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

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
def greet(name):
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