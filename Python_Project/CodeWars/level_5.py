#Simple Pig Latin
def pig_it(text):
    return " ".join( letter if letter == "!" or letter == "?"  else (letter[1:] + letter[0] + "ay") for  letter in text.split(" "))
