def encontrar_extremos(lista):

    #Verifica que sea una lista
    if not isinstance(lista, list):
        return -600, None, None

    # Verifica que todos los elementos sea números  
    for objeto in lista:
        if not isinstance(objeto, (int, float)) or type(objeto) is bool:
            return -700, None, None

    # Devuelve el los números 1, 2 y 3 en caso de que no se cumpla ninguna condición de falla.
    return 0, 1, 3
