def multiplicar_indices (lista):
    if isinstance (lista, list):
        return indices_aux (lista, 0)
    else:
        return "Error"

def indices_aux (lista, indice):
    if lista == []:
        return []
    elif len(lista) >= 1:
        return [indice * lista[0]] + indices_aux (lista[1:], indice + 1)
    else:
        return indices_aux (lista[1:], indice + 1)

#####################################################
def lista_potencia (lista):
    if isinstance (lista, list):
        return potencia_aux (lista, 1)
    else:
        return "Error"

def potencia_aux (lista, pot):
    if lista == []:
        return 0
    elif isinstance (lista[0], list):
        return potencia_aux(lista[0] + lista[1:], pot)
    else:
        return (lista[0]**pot) + potencia_aux(lista[1:], pot + 1)
###################################################

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
