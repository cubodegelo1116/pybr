traducao = {
    "se": "if",
    "senao": "else",
    "enquanto": "while",
    "para": "for",
    "em": "in",
    "imprimir": "print",
    "verdadeiro": "True",
    "falso": "False"
}

def traduzir(codigo):
    for pt, en in traducao.items():
        codigo = codigo.replace(pt, en)
    return codigo

def executar(arquivo):
    with open(arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    codigo_py = traduzir(codigo)
    exec(codigo_py)
