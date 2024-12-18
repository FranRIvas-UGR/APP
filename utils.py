def resolver_mochila_limited(articulos, presupuesto):
    # Inicializamos una fila de dp de tamaño presupuesto + 1
    dp = [0] * (presupuesto + 1)

    # Rellenamos el dp para cada artículo
    for articulo in articulos:
        precio = int(articulo['precio'])
        valor = int(articulo['valoracion'])

        # Llenamos el dp desde el presupuesto hacia abajo
        for w in range(presupuesto, precio - 1, -1):
            dp[w] = max(dp[w], dp[w - precio] + valor)

    # Reconstrucción de la solución
    seleccionados = []
    w = presupuesto
    for i in range(len(articulos) - 1, -1, -1):  # Iteramos en reversa
        articulo = articulos[i]
        precio = int(articulo['precio'])
        valor = int(articulo['valoracion'])

        # Si el artículo fue seleccionado, es decir, si el valor cambia al incluirlo
        if w >= precio and dp[w] == dp[w - precio] + valor:
            seleccionados.append({**articulo, "cantidad": 1})  # Se selecciona una unidad
            w -= precio  # Restamos el precio del artículo seleccionado

    # Calcular el precio total
    precio_total = sum(item['precio'] * item['cantidad'] for item in seleccionados)
    
    # Verificación de los artículos seleccionados
    if not seleccionados:
        print("No se seleccionaron artículos.")

    if precio_total > presupuesto:
        return {
            "articulos_seleccionados": [],
            "valoracion_total": 0,
            "precio_total": 0
        }

    return {
        "articulos_seleccionados": seleccionados,
        "valoracion_total": dp[presupuesto],
        "precio_total": precio_total
    }


def resolver_mochila_limited_presupuesto(articulos, presupuesto):
    # Convertimos presupuesto y precios a enteros (multiplicamos por 100)
    presupuesto = int(presupuesto * 100)
    for articulo in articulos:
        try:
            articulo['precio'] = int(float(articulo['precio']) * 100)
            articulo['valoracion'] = int(float(articulo['valoracion']))
        except ValueError:
            raise ValueError(f"Invalid price or valuation for article: {articulo}")

    # Ordenamos los artículos por relación valor/precio descendente
    articulos = sorted(articulos, key=lambda x: x['valoracion'] / x['precio'], reverse=True)

    # Inicializamos variables
    mejor_valoracion = 0
    mejor_seleccion = []
    mejor_precio_total = 0
    cache = {}

    # Función recursiva para explorar combinaciones posibles con poda
    def backtrack(seleccionados, valoracion_actual, precio_actual, index):
        nonlocal mejor_valoracion, mejor_seleccion, mejor_precio_total

        # Si excede el presupuesto, no es válido
        if precio_actual > presupuesto:
            return

        # Si llegamos al final de los artículos, actualizamos la mejor solución
        if index == len(articulos):
            if valoracion_actual > mejor_valoracion:
                mejor_valoracion = valoracion_actual
                mejor_seleccion = seleccionados[:]
                mejor_precio_total = precio_actual
            return

        # Estado actual para memoización
        estado = (index, precio_actual)
        if estado in cache and cache[estado] >= valoracion_actual:
            return
        cache[estado] = valoracion_actual

        # Poda por estimación de valor potencial máximo
        valor_potencial = valoracion_actual
        peso_restante = presupuesto - precio_actual
        for i in range(index, len(articulos)):
            precio = articulos[i]['precio']
            valor = articulos[i]['valoracion']
            if precio <= peso_restante:
                valor_potencial += valor
                peso_restante -= precio
            else:
                valor_potencial += (valor / precio) * peso_restante
                break
        if valor_potencial <= mejor_valoracion:
            return

        # Opción 1: No incluir el artículo actual
        backtrack(seleccionados, valoracion_actual, precio_actual, index + 1)

        # Opción 2: Incluir el artículo actual
        articulo = articulos[index]
        seleccionados.append({**articulo, "cantidad": 1})
        backtrack(seleccionados, valoracion_actual + articulo['valoracion'], precio_actual + articulo['precio'], index + 1)
        seleccionados.pop()

    # Iniciamos la búsqueda
    backtrack([], 0, 0, 0)

    # Convertimos los precios de nuevo a formato flotante para el resultado final
    for articulo in mejor_seleccion:
        articulo['precio'] = articulo['precio'] / 100
    mejor_precio_total = mejor_precio_total / 100
    
    for articulo in articulos:
        try:
            articulo['precio'] = float(articulo['precio']) / 100
        except ValueError:
            raise ValueError(f"Invalid price or valuation for article: {articulo}")

    return {
        "articulos_seleccionados": mejor_seleccion,
        "valoracion_total": mejor_valoracion,
        "precio_total": mejor_precio_total
    }

