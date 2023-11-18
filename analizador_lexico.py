# Resultado del análisis
resultado_lexema = []
# aqui declarar todas las normas

opAritmeticos = ["-", "+", "!", "*", "^", "/", "mod"]
opLogicos = ["and", "or", "not", "xor", "implies", "equivalent"]
opRelacionales = ["=", "<>", "<", "<=", ">", ">="]
opAsignacion = [":=", "*=", "/=", "+=", "-=", "->"]
simbolosAbrir = ["(", "[", "{", "'", '"']
simbolosCerrar = [")", "]", "}", "'", '"']
terminales = [";", ":"]
separadores = [";" r"\n"]
palabrasBucle = ["for", "while", "do", "end do", "od"]
palabrasDecision = ["if", "elif", "fi", "case", "end case"]
palabrasClases = ["module", "end module"]
letras = [
    "a",
    "A",
    "b",
    "B",
    "c",
    "C",
    "d",
    "D",
    "e",
    "E",
    "f",
    "F",
    "g",
    "G",
    "h",
    "H",
    "i",
    "I",
    "j",
    "J",
    "k",
    "K",
    "l",
    "L",
    "m",
    "M",
    "n",
    "N",
    "ñ",
    "Ñ",
    "o",
    "O",
    "p",
    "P",
    "q",
    "Q",
    "r",
    "R",
    "s",
    "S",
    "t",
    "T",
    "u",
    "U",
    "v",
    "V",
    "w",
    "W",
    "x",
    "X",
    "y",
    "Y",
    "z",
    "Z",
]
numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["$", "_"]

token = (
    opAritmeticos
    + opLogicos
    + opRelacionales
    + opAsignacion
    + simbolosAbrir
    + simbolosCerrar
    + terminales
    + separadores
    + palabrasBucle
    + palabrasClases
    + palabrasDecision
    + letras
    + numeros
    + simbolos
)


def analizador_lexico(data):
    palabras = data.split()
    cont = 1

    for palabra in palabras:
        if palabra in token:
            if palabra in opAritmeticos:
                resultado_lexema.append(f"Operador Aritmetico: {palabra}")
            elif palabra in opLogicos:
                resultado_lexema.append(f"Operador Logico: {palabra}")
            elif palabra in opRelacionales:
                resultado_lexema.append(f"Operador Relacional: {palabra}")
            elif palabra in opAsignacion:
                resultado_lexema.append(f"Operador de Asignacion: {palabra}")
            elif palabra in simbolosAbrir:
                resultado_lexema.append(f"Simbolo de Apertura: {palabra}")
            elif palabra in simbolosCerrar:
                resultado_lexema.append(f"Simbolo de Cierre: {palabra}")
            elif palabra in terminales:
                resultado_lexema.append(f"Terminal: {palabra}")
            elif palabra in separadores:
                resultado_lexema.append(f"Separador: {palabra}")
            elif palabra in palabrasBucle:
                resultado_lexema.append(f"Palabra de Bucle: {palabra}")
            elif palabra in palabrasDecision:
                resultado_lexema.append(f"Palabra de Decision: {palabra}")
            elif palabra in palabrasClases:
                resultado_lexema.append(f"Palabra de Clase: {palabra}")
            elif palabra in numeros:
                resultado_lexema.append(f"Numero: {palabra}")
            elif palabra in simbolos:
                resultado_lexema.append(f"Simbolo: {palabra}")
            else:
                resultado_lexema.append(f"Identificador: {palabra}")
        else:
            flagError = False
            if palabra[0] in letras:
                for caracter in palabra:
                    if (
                        caracter not in numeros
                        and caracter not in letras
                        and caracter not in simbolos
                    ):
                        flagError = True
                        break
            else:
                flagError = True
            if flagError:
                resultado_lexema.append(f"Error: {palabra}")
            else:
                resultado_lexema.append(f"Identificador: {palabra}")
        if cont < len(palabras):
            resultado_lexema.append(f" => ")
        cont += 1
    if palabras[-1] not in terminales:
        resultado_lexema.append(f" => Error: Falta el terminal al final de la línea ")

    return resultado_lexema


if __name__ == "__main__":
    while True:
        data = input("Ingrese: ")
        resultado_lexema = []  # Reiniciar la lista en cada iteración
        analizador_lexico(data)
        print("".join(resultado_lexema))
