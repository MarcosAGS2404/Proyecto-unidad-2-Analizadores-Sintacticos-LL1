# parser_lr.py
# Analizador sintáctico LR para MiniC usando PLY

import ply.yacc as yacc
from lexer_ply import tokens

# Reglas gramaticales

def p_program(p):
    'program : stmt_list'
    pass

def p_stmt_list_multiple(p):
    'stmt_list : stmt_list stmt'
    pass

def p_stmt_list_single(p):
    'stmt_list : stmt'
    pass

def p_stmt_declaration(p):
    'stmt : INT ID SEMICOLON'
    pass

def p_stmt_assignment(p):
    'stmt : ID EQUAL expr SEMICOLON'
    pass

def p_stmt_if(p):
    'stmt : IF LPAREN expr RPAREN block else_stmt'
    pass

def p_stmt_while(p):
    'stmt : WHILE LPAREN expr RPAREN block'
    pass

def p_else_stmt(p):
    '''else_stmt : ELSE block
                 | empty'''
    pass

def p_block(p):
    'block : LBRACE stmt_list RBRACE'
    pass

# Operaciones binarias
def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr LT expr
            | expr GT expr'''
    pass

def p_expr_group(p):
    'expr : LPAREN expr RPAREN'
    pass

def p_expr_number(p):
    'expr : NUMBER'
    pass

def p_expr_id(p):
    'expr : ID'
    pass

# Producción vacía
def p_empty(p):
    'empty :'
    pass

# Manejador de errores sintácticos
def p_error(p):
    print("Syntax error")

# Construcción del parser
parser = yacc.yacc()

