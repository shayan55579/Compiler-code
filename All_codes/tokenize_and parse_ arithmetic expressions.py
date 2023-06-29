
"""
@author: shayan
The code defines a lexer using the ply.lex library to tokenize and parse arithmetic
expressions in infix notation. It converts the infix expression to postfix notation using the
Shunting Yard algorithm and then evaluates the postfix expression to obtain the result.
"""
import ply.lex as lex

tokens = ('ID', 'NUMBER', 'DECIMAL', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    t.value = str(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def prec(op1, op2):
    pm = '+-'
    md = '*/'
    same = (op1 in pm and op2 in pm) or (op1 in md and op2 in md)
    if same or (op1 in md and op2 in pm):
        return 1
    return -1

def in2pos(data):
    lexer.input(data)

    op = []
    operators = {'PLUS': '+', 'MINUS': '-', 'TIMES': '*', 'DIVIDE': '/'}
    postfix = ""

    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type in ('ID', 'NUMBER'):
            postfix += str(tok.value) + ' '
        elif tok.type in operators:
            _op = operators[tok.type]
            while op and prec(op[-1], _op) == 1:
                postfix += op.pop() + ' '
            op.append(_op)

    while op:
        postfix += op.pop() + ' '

    return postfix

data = '12.45 + -4.5 * xy - 12 / y'
print(data)
i2p = in2pos(data)
print(i2p)

