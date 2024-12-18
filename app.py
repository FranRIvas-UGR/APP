# app.py
from database import obtener_articulos_por_categoria, get_categorias
from utils import resolver_mochila_limited_presupuesto
from database import insertar_categoria, insertar_articulo, crear_tablas
import csv, random


def leer_csv():
    crear_tablas()
    print("Leyendo datos de productos.csv...")
    categorias = set()
    with open('productos.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            categoria_nombre = row["Categoría Nombre"]
            producto_nombre = row["Producto Nombre"]
            precio = float(row["Precio"])
            
            # Añadimos la categoría a la lista de categorías
            if categoria_nombre not in categorias:
                categorias.add(categoria_nombre)
                # Insertamos la categoría y el artículo en la base de datos
                insertar_categoria(categoria_nombre)
                
            val=random.randint(1, 10)    
            insertar_articulo(producto_nombre, precio, categoria_nombre, valoracion=val)


def main():
    categorias = []

    categorias_dict = get_categorias()
    categorias_dict = {k: v for k, v in categorias_dict.items()}

    print("Seleccione las categorías (separadas por comas):")
    for id, nombre in categorias_dict.items():
        print(f"{id}: {nombre}")

    seleccion = input("Ingrese los IDs de las categorías seleccionadas: ")
    selected_ids = [int(id.strip()) for id in seleccion.split(",") if id.strip().isdigit()]

    if not selected_ids:
        print("Debe seleccionar al menos una categoría.")
        return
    else:
        categorias = selected_ids
    
    print(f"Categorías seleccionadas: {categorias}")
    
    articulos = []
    for categoria in categorias:
        articulos.append({'categoria_id': categoria, 'articulos_categoria': obtener_articulos_por_categoria(categoria)})
        
        
    # print("--------------------\n")
    # Verificación de los artículos obtenidos
    #print(f"Artículos obtenidos: {articulos}")
    
    # Convertimos los artículos a una lista de diccionarios
    keys = ["id", "nombre", "precio", "valoracion", "categoria_id", "min", "max"]
    articulos_dict = []
    for articulo in articulos:
        for item in articulo['articulos_categoria']:
            if item[0] != 'id':  # Skip the header row
                articulos_dict.append(dict(zip(keys, item)))
    
    print("--------------------\n")
    
    # Verificación de los artículos convertidos a diccionarios
    #print(f"Artículos convertidos a diccionarios: {articulos_dict}")

    # Optimizamos las compras
    #resultado = resolver_mochila_limited(articulos_dict, presupuesto)
    
    #resultado2 = resolver_mochila_limited_presupuesto(articulos_dict, presupuesto)
    
    # Imprimimos los resultados de manera más atractiva
    #print("\nResultado de la optimización:")
    #imprimir_resultado_optimizacion(resultado)
    
    #print("\nResultado de la optimización 2:")
    #imprimir_resultado_optimizacion(resultado2)
    
    # Decido que quiero 3 articulos de una categoría y 2 de otra como máximo
    
    presupuesto = input("Ingrese el presupuesto: ")
    presupuesto = float(presupuesto)
    presupuestos_parciales = {}
    if (len(selected_ids) > 1):
        seRepartePresupuesto = input("¿Desea repartir el presupuesto entre las categorías? (s/n): ")
        if seRepartePresupuesto == 's':
            for categoria in categorias:
                presupuesto_categoria = input(f"Ingrese el presupuesto para la categoría {categorias_dict[categoria]}: ")
                presupuestos_parciales[categoria] = float(presupuesto_categoria)
        else:
            presupuestos_parciales = {categoria: float(presupuesto) / len(categorias) for categoria in categorias}
    else:
        presupuestos_parciales = {categorias[0]: presupuesto}
                
    # Ingresar el número de artículos a seleccionar por categoría
    dic_num_articulos = {}
    for categoria in categorias:
        num_articulos = input(f"Ingrese el número de artículos a seleccionar para la categoría {categorias_dict[categoria]}: ")
        dic_num_articulos[categoria] = int(num_articulos)

    print(presupuestos_parciales)
    print("\nResultado de la optimización 3:")
    for categoria in categorias:
        resultado_categoria = calcular_productos_categoria(articulos_dict, presupuestos_parciales[categoria], categoria, dic_num_articulos[categoria])
        imprimir_resultado_optimizacion(resultado_categoria)
        print("\n")
    
    
def imprimir_resultado_optimizacion(resultado):
        print("Artículos seleccionados:")
        precio_total = 0
        for articulo in resultado['articulos_seleccionados']:
            if articulo['cantidad'] > 0:
                print(f"  - {articulo['nombre']} (Cantidad: {articulo['cantidad']}, Precio: {articulo['precio']}, Valoración: {articulo['valoracion']})")
                precio_total += articulo['cantidad'] * articulo['precio']
        print(f"Valoración total: {resultado['valoracion_total']}")
        print(f"Precio total: {precio_total}")



def calcular_productos_categoria(diccionario_articulos_general, presupuesto_reducido, categoria_id ,num_articulos):
    articulos_cat = [articulo for articulo in diccionario_articulos_general if articulo['categoria_id'] == categoria_id]
    bebidas = resolver_mochila_limited_presupuesto(articulos_cat, presupuesto_reducido)
    
    bebidas_result = {'articulos_seleccionados': [], 'valoracion_total': 0, 'precio_total': 0}
    
    # Solo selecciono 2 bebidas, con sus precios y valoraciones. Esttructura de bebidas_result: {'articulos_seleccionados': {'nombre': {'precio': precio, 'valoracion': valoracion}}, 'valoracion_total': valoracion_total, 'precio_total': precio_total}
    for articulo in bebidas['articulos_seleccionados']:
        if len(bebidas_result['articulos_seleccionados']) >= num_articulos:
            break
        if articulo['cantidad'] > 0:
            bebidas_result['articulos_seleccionados'].append({'nombre': articulo['nombre'], 'precio': articulo['precio'], 'valoracion': articulo['valoracion'], 'cantidad': articulo['cantidad']})
            bebidas_result['valoracion_total'] += articulo['valoracion']
            bebidas_result['precio_total'] += articulo['precio']
            
    return bebidas_result    


if __name__ == '__main__':
    print("Bienvenido al sistema de recomendación de compras.")
    opcion = input("¿Desea leer los datos de productos desde el archivo productos.csv (1) o usar la app (2) ?")
    if opcion == '1':
        leer_csv()
    elif opcion == '2':
        main()
    else:
        print("Opción no válida.") 