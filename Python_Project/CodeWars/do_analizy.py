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