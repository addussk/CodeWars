# Do Analizy
# def calculator(x, y, op):
#   return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'

# def calculator(x,y,op):
#     try:
#         assert op in "+-*/"
#         return eval('%d%s%d' % (x, op, y))
#     except:
#         return "unknown value"

# Who ate the cookie?
def cookie(x):
    return "Who ate the last cookie? It was %s!" % {str:"Zach", float:"Monica", int:"Monica"}.get(type(x), "the dog")

# Draw stairs
def draw_stairs(n):
    return '\n'.join(' '*i+'I' for i in range(n))

# Heads and Legs
def animals(heads, legs):
    ch, co = 2 * heads - legs / 2, legs / 2 - heads
    return (0, 0) if heads == 0 and legs == 0 else (ch, co) if ch == int(ch) and co == int(co) and ch >= 0 and co >= 0 else 'No solutions'

# Did she say hallo?
def validate_hello(greetings):
    return any(x in greetings.lower() for x in ['hello','ciao','salut','hallo','hola','ahoj','czesc'])

# Training JS #18: Methods of String object--concat() split() and its good friend join()
def split_and_merge(string_, separator):
    return # your code here


def any_arrows(arrows):
    return any(not i.get("damaged", False) for i in arrows)