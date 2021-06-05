def clasificacion_huevos(lista: float):
    A = 0
    AA = 0
    AAA = 0
    BC = 0
    for elem in lista:
        if elem >= 55 and elem < 60:
            A += 1
        if elem >= 60 and elem < 69:
            AA += 1
        if elem >= 69:
            AAA += 1
        if elem < 53: 
            BC += 1
    return calcular_bandejas(A, AA, AAA, BC)

def calcular_bandejas(A: int, AA: int, AAA: int, BC: int):
    bandeja_A = A // 30
    bandeja_AA = AA // 24
    bandeja_AAA = AAA // 14
    bandeja_BC = BC // 30

    lista_cajas = [
            {
                "tipo_huevo": "A",
                "numero_huevos": A,
                "numero_bandejas": bandeja_A
              },
               {
                "tipo_huevo": "AA",
                "numero_huevos": AA,
                "numero_bandejas": bandeja_AA
                },
                {
                "tipo_huevo": "AAA",
                "numero_huevos": AAA,
                "numero_bandejas": bandeja_AAA
                },
                {"tipo_huevo": "BC",
                "numero_huevos": BC,
                "numero_bandejas": bandeja_BC
                }]

    return lista_cajas

lista = [46.5, 60.8, 58.7, 70.0, 49.8]

print(clasificacion_huevos(lista))