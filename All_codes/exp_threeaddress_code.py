
tokens = (
    'NAME','NUMBER',
    'PLUS','MINUS','TIMES','DIVIDE','EQUALS', 'POW',
    'LPAREN','RPAREN',
    )

# Tokens

t_POW     = r'\^'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMBER  = r'[1-9][0-9]*' #r'\d+'

# def t_NUMBER(t):
#     r'\d+'
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         print("Integer value too large %d", t.value)
#         t.value = 0
#     return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    ('right','POW'),
    )

# dictionary of names
names = { }
n = 1
# 1- (operator, operand1, operand2, destination)
# 2- destination = operand1 operator operand2
code = []

def getTemp():
    global n
    var = f't{n}'
    # بررسی یکتایی نام متغیر موقت
    n += 1
    return var

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    # cd = f'{t[1]} = {t[3]}' # a = t8
    cd = f'(=,{t[3]}, None, {t[1]})'
    code.append(cd)

def p_statement_expr(t):
    'statement : expression'
    global n, code
    
    #کدهای سه آدرسه را در خروجی نمایش بده
    for cd in code:
        print(cd)
    
    #برای ورودی بعدی آماده شو
    code = []
    n = 1

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POW expression'''
    temp = getTemp()
    # cd = f'{temp} = {t[1]} {t[2]} {t[3]}'
    cd = f'({t[2]}, {t[1]}, {t[3]}, {temp})'
    t[0] = temp
    code.append(cd)
    
def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    temp = getTemp()
    # cd = f'{temp} = -{t[2]}'
    cd = f'(-, {t[2]}, None, {temp})'
    t[0] = temp
    code.append(cd)

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    t[0] = t[1]
    
def p_error(t):
    print("Syntax error at '%s'" % t)

import ply.yacc as yacc
# parser = yacc.yacc()
parser = yacc.yacc(debug=True)

while True:
    try:
        s = input('Exp => ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
