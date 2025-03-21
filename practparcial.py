def mejor_ajuste(particiones_memoria, solicitudes, indice_inicio=0):
    # Copia la memoria para evitar modificar la original
    nueva_memoria = particiones_memoria.copy()
    
    asignaciones = {}  # Almacenará las asignaciones de solicitudes
    
    for solicitud in solicitudes:
        mejor_idx = -1
        mejor_tamano = float('inf')
        
        # Primera búsqueda desde indice_inicio
        for i in range(indice_inicio, len(nueva_memoria)):
            base, limite = nueva_memoria[i]
            tamano = limite - base
            if solicitud <= tamano and tamano < mejor_tamano:
                mejor_tamano = tamano
                mejor_idx = i
        
        # Si no se encontró espacio desde indice_inicio, buscar en toda la tabla
        if mejor_idx == -1:
            mejor_tamano = float('inf')  # Resetear el mejor tamaño
            for i in range(len(nueva_memoria)):
                base, limite = nueva_memoria[i]
                tamano = limite - base
                if solicitud <= tamano and tamano < mejor_tamano:
                    mejor_tamano = tamano
                    mejor_idx = i
        
        if mejor_idx != -1:
            base, limite = nueva_memoria[mejor_idx]
            asignaciones[solicitud] = (base, base + solicitud)
            nueva_memoria[mejor_idx] = (base + solicitud, limite - solicitud)  # Reducir el límite correctamente
        else:
            asignaciones[solicitud] = None  # No se pudo asignar
    
    return asignaciones, nueva_memoria

# Ejemplo de ejecución
tabla = [(0, 100), (150, 300), (350, 500)]  # Base y límite de cada partición
solicitudes = [150, 110, 30]  # Tamaños de solicitudes
indice_inicio = 0  # Índice desde donde iniciar la búsqueda

asignaciones, nueva_tabla = mejor_ajuste(tabla, solicitudes, indice_inicio)

print("Asignaciones de solicitudes:")
for solicitud, asignacion in asignaciones.items():
    print(f"Solicitud {solicitud} -> {asignacion if asignacion else 'No asignado'}")

print("\nNueva tabla de memoria:")
print(nueva_tabla)