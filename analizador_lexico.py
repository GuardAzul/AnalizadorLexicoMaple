# Resultado del análisis
resultado_lexema = []
#aqui declarar todos los conjuntos
#Aqui estuvo castro
# Palabras reservadas
reservadas = [
    'include', 'using', 'namespace', 'std', 'cout', 'cin', 'get', 'endl',
    'else', 'if', 'return', 'void', 'while', 'for'
]

#operadores de asignacion
opAsignacion = []

def analizador_lexico(data):
    i = 0
    n = len(data)
    while i < n:
        if data[i].isspace():
            i += 1
            continue
        elif data[i].isalpha() or data[i] == '_':
            lexema = data[i]
            i += 1
            while i < n and (data[i].isalnum() or data[i] == '_'):
                lexema += data[i]
                i += 1
            if lexema in reservadas:
                resultado_lexema.append(f'Palabra Reservada: {lexema}')
            else:
                resultado_lexema.append(f'Identificador: {lexema}')
        elif data[i].isdigit():
            numero = ''
            while i < n and (data[i].isdigit() or data[i] == '.'):
                numero += data[i]
                i += 1
            resultado_lexema.append(f'Entero: {numero}')
        else:
            # Manejar otros tokens
            if data[i:i+2] == '<<' or data[i:i+2] == '>>':
                resultado_lexema.append(f'Operador: {data[i:i+2]}')
                i += 2
            else:
                resultado_lexema.append(f'Operador: {data[i]}')
                i += 1

    return resultado_lexema

if __name__ == '__main__':
    while True:
        data = input("Ingrese: ")
        analizador_lexico(data)
        print(resultado_lexema)
