tokens = (
    'ZERO','ONE',
    )

# Tokens

t_ZERO    = r'0'
t_ONE     = r'1'

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

def p_statement_expr(p):
    'statement : expression'
    print(f'Decimal value of [{binary}] with {number} digits => {p[1]}')

def p_expression_expr(p):
    'expression : dig expression'
    global power
    p[0] = p[1]*(2**power)+p[2]
    power += 1

def p_expression_expr_d(p):
    'expression : dig'
    global power
    p[0] = p[1]
    power += 1

def p_expression_dig(p):
    '''dig : ONE
         | ZERO'''
    global number, binary
    p[0] = 0 if p[1]=='0' else 1 
    number += 1
    binary = binary+p[1]

def p_error(t):
    print("Syntax error at '%s'" % t)

import ply.yacc as yacc
parser = yacc.yacc()
# parser = yacc.yacc(debug=True)

while True:
    try:
        number = 0
        power = 0
        binary = ''
        s = input('Input a binary number => ')   # Use raw_input on Python 2
    except EOFError:

        break
    parser.parse(s)
