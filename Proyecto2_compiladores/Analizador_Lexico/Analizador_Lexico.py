# lexer_ply.py
# Analizador l�xico para el lenguaje MiniC usando PLY

import ply.lex as lex

# Lista de tokens reconocidos por el lenguaje
tokens = (
    'ID', 'NUMBER', 'IF', 'ELSE', 'WHILE', 'INT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUAL',
    'LT', 'GT', 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON'
)

# Expresiones regulares para tokens de un solo car�cter
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'='
t_LT = r'<'
t_GT = r'>'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'

# Palabras reservadas
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'int': 'INT',
}

# Identificadores o palabras reservadas
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Determina si es palabra reservada
    return t

# N�meros enteros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espacios, tabulaciones y saltos de l�nea
t_ignore = ' \t\r\n'

# Manejador de errores l�xicos
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construcci�n del analizador l�xico
lexer = lex.lex()

