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
