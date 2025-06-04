def filtrar_positivos(lista):
    positivos = [x for x in lista if x >= 0]
    return positivos

numeros = [8, -13, 889, -6, -450, 10, 81]
positvos = filtrar_positivos(numeros)
print("Números positivos:", positvos)
