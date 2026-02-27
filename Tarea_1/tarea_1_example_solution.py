# Códigos de retorno solicitados
exito = 0
no_lista = -600
no_numeros = -700
lista_vacia = -800
lista_larga = -900


# Se define el segundo método solicitado, utiliza como parámetro lista_numeros
# que debe ser en formato lista, se verifican las condiciones de falla primero,
# si alguna de estas se cumple se devuelve el código de error correspondiente y
# None 2 veces, si no se cumple ninguna condición de falla, se obtienen los
# valores mínimos y máximos de la lista y se devuelven junto con el código de
# éxito en el orden corcrespondiente
def encontrar_extremos(lista_numeros):

    # Verifica que sea una lista
    if not isinstance(lista_numeros, list):
        return no_lista, None, None

    # Verifica que todos los elementos sea números
    for elemento in lista_numeros:
        if not isinstance(elemento, (int, float)) or type(elemento) is bool:
            return no_numeros, None, None

    # Verifica que no tenga más de 15 elementos
    if len(lista_numeros) > 15:
        return lista_larga, None, None

    # Verifica que la lista no esté vacía
    if len(lista_numeros) == 0:
        return lista_vacia, None, None

    # Se calculan los extremos solicitados
    minimo = min(lista_numeros)
    maximo = max(lista_numeros)

    # Devuelve el código de éxito y los valores mínimo y máximo en caso de que
    # no se cumpla ninguna condición de falla.
    return exito, minimo, maximo
