# Resultado del análisis
resultado_lexema = []
#aqui declarar todos los conjuntos
#Aqui estuvo castro
#operadores de asignacion
opAritmeticos = ['-','+','!','*','^','/', 'mod']
opLogicos =['and', 'or', 'not', 'xor', 'implies', 'equivalent']
opRelacionales = ['=', '<>', '<', '<=', '>', '>=']
opAsignacion = [':=', '*=', '/=', '+=', '-=', '->']
simbolosAbrir = ['(', '[', '{', "'", '"']
simbolosCerrar = [')', ']', '}', "'", '"']
terminales = [';', ':']
sepadores = [';' r"\n"]
palabrasBucle = ['for', 'while', 'do', 'end do', 'od']
palabrasDecision = ['if', 'elif', 'fi', 'case', 'end case']
palabrasClases = ['module', 'end module']
letras = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','m','M','n','N','ñ','Ñ','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','w','W','x','X','y','Y','z','Z']
numeros = [0, 1,2,3,4,5,6,7,8,9]
simbolos = ['$']

token = opAritmeticos 

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
            if lexema in token:
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