
"""
Simple Statement Lexical Analyzer
Compilation Technique - Project 1
Language: Pascal-like
"""

import ply.lex as lex

reserved = {
    "PROGRAM": "PROGRAM",
    "BEGIN": "BEGIN",
    "WRITELN": "WRITELN",
    "END": "END",
}

tokens = (
    "PROGRAM",
    "BEGIN",
    "WRITELN",
    "END",
    "ID",
    "STRING",
    "SEMICOLON",
    "LPAREN",
    "RPAREN",
    "DOT",
)

t_SEMICOLON = r";"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_DOT = r"\."


def t_STRING(t):
    r"'([^'\n]|'')*'"
    return t


def t_ID(t):
    r"[A-Za-z_][A-Za-z0-9_]*"

    t.type = reserved.get(t.value.upper(), "ID")

    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t\r"


def t_error(t):
    print(
        f"Lexical error: illegal character {t.value[0]!r} "
        f"at line {t.lexer.lineno}"
    )
    t.lexer.skip(1)


lexer = lex.lex()


if __name__ == "__main__":

    with open("sample1.txt", "r", encoding="utf-8") as source_file:
        source_code = source_file.read()

    print("SOURCE CODE:")
    print(source_code)

    print("\nTOKENS:")
    print(f"{'TOKEN TYPE':<12} {'TOKEN VALUE':<22} {'LINE':>4}")
    print("-" * 42)

    lexer.lineno = 1
    lexer.input(source_code)

    while True:
        token = lexer.token()

        if token is None:
            break

        print(
            f"{token.type:<12} "
            f"{token.value:<22} "
            f"{token.lineno:>4}"
        )
