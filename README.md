# Proyecto-unidad-2-Analizadores-Sintacticos-LL1

Proyecto Unidad 2 – Compiladores  
## Analizador Léxico y Sintáctico para el Lenguaje MiniC

---

## 📘 Descripción General

Este proyecto tiene como finalidad desarrollar un compilador parcial para un subconjunto del lenguaje *MiniC, implementando las fases de análisis léxico y sintáctico. Se utilizaron herramientas como **PLY (Python Lex-Yacc)* para construir:

- Un *analizador léxico* que reconoce palabras clave, identificadores, operadores y símbolos del lenguaje.
- Un *parser LR* basado en la gramática definida y transformada del lenguaje MiniC.
- Un *esquema de parser LL(1)* desarrollado para fines de comparación con el parser LR.
- *Árboles de derivación* generados gráficamente para representar la estructura de las cadenas válidas.

El proyecto demuestra el uso de gramáticas libres de contexto (CFG), su transformación y aplicación práctica mediante parsers.
## ⚙️ Requisitos

- Python 3.7 o superior
- Biblioteca PLY (Python Lex-Yacc)

Instalación rápida con pip:


pip install ply
⚙️ Características del Sistema
El sistema desarrollado corresponde a un analizador léxico y sintáctico para un subconjunto del lenguaje MiniC, e incluye las siguientes funcionalidades principales:

🔹 1. Análisis Léxico (Lexer con PLY)
Reconoce correctamente:

Palabras clave (int, if, else, while, etc.)

Identificadores (x, a, variable1, etc.)

Números enteros y reales

Operadores aritméticos y relacionales (+, -, *, /, <, >, ==, etc.)

Símbolos especiales (;, (, ), {, }, =)

Ignora espacios y saltos de línea

Reporta errores léxicos (tokens no reconocidos)
