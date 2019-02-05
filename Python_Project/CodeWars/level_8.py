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