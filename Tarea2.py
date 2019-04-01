def pares_num (num):
    if isinstance (num, int):
        par = lambda digito : (digito  % 10) % 2 == 0
        impar = lambda digito : (digito  % 10) % 2 == 1
        return pares_num_aux (num, par), impar_num_aux(num, impar)
    else :
        "Error"

def pares_num_aux (num, par):
    if num == 0:
        return []
    elif par(num):
        return [num % 10] + pares_num_aux (num // 10, par)
    else:
        return pares_num_aux (num//10, par)

def impar_num_aux (num, impar):
    if num == 0:
        return []
    elif impar(num):
        return [num % 10] + impar_num_aux (num // 10, impar)
    else:
        return impar_num_aux (num//10, impar)
#####################################################
def num_palindromo (num):
    if isinstance (num, int):
        return cantidad(num, num, num, 0, 0)
    else:
        "Error"

def cantidad (num, comparacion, contrario, comparar2, exp):
    if num == contrario:
        return True
    elif num > 0:
        return cantidad (num, comparacion // 10, contrario, exp + 1)
    else:
        return alrevez (num, comparacion, contrario, comparar2, exp)
        


def alrevez (num, comparacion, contrario, exp):
    if num == contrario:
        return cantidad (num, comparacion, contrario, exp) 
    elif comparar2 > 0 :
        return alrevez(num, comparacion, contrario + ((comparacion % 10)*10**exp), comparar2 // 10, exp - 1) 
    else:
        return False
###################################################
def cadena_texto (texto):
    if isinstance (texto, str):
        return texto_aux (texto)
    else:
        return "Error"

def texto_aux(texto):

    if texto == "":
        return 0
    elif texto [0] == "A" or texto [0] == "a" or texto [0] == "E" or texto [0] == "e" or texto [0] == "I" or texto [0] == "i" or texto [0] == "O" or texto [0] == "o" or texto [0] == "U" or texto [0] == "u":
        return texto_aux(texto[1:])
    else :
        return (1) + texto_aux(texto[1:])
##################################################33
def intercambiar_indices (lista):
    if isinstance (lista, list) and len (lista) % 2 == 0:
        return indices_aux(lista)
    else :
        return "Error"


def indices_aux (lista):
    if lista == []:
        return []
    elif len (lista) >= 1:
        return [lista [1]] + [lista[0]] + indices_aux (lista[2:])
    else:
        return indices_aux (lista[2:])
