def validar_cuit(cuit: str) -> bool:
    # Eliminar posibles guiones o espacios
    cuit = cuit.replace("-", "").strip()

    # Debe tener 11 dígitos
    if not cuit.isdigit() or len(cuit) != 11:
        return False

    # Convertir a lista de enteros
    numeros = [int(d) for d in cuit]

    # Pesos según AFIP
    pesos = [5, 4, 3, 2, 7, 6, 5, 4, 3, 2]

    # Calcular suma ponderada de los 10 primeros dígitos
    suma = sum([a*b for a, b in zip(numeros[:-1], pesos)])

    # Calcular verificador
    resto = suma % 11
    verificador = 11 - resto if resto != 0 else 0
    if verificador == 11:
        verificador = 0
    elif verificador == 10:
        verificador = 9

    # Comparar con último dígito
    return numeros[-1] == verificador


# --- Programa principal con loop ---
print("Validador de CUIT/CUIL (escriba 'salir' para terminar)\n")

while True:
    cuit_ingresado = input("Ingrese un CUIT/CUIL: ")

    if cuit_ingresado.lower() == "salir":
        print("👋 Programa finalizado.")
        break

    if validar_cuit(cuit_ingresado):
        print("✅ El CUIT/CUIL es válido\n")
    else:
        print("❌ El CUIT/CUIL es inválido\n")
