# app.py
from database import crear_tablas, insertar_categoria, insertar_articulo, obtener_articulos_por_categoria
from utils import resolver_mochila_limited
import csv
import random

def main():
    # Inicializamos la base de datos
    #crear_tablas()
    
    #categorias = set()
    
    """ # Leemos los datos de un archivo CSV
    print("Leyendo datos de productos.csv...")
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
            insertar_articulo(producto_nombre, precio, categoria_nombre, valoracion=val) """
    
    # Obtenemos todos los artículos para las categorías seleccionadas
    print("Obteniendo artículos de las categorías seleccionadas...")
    categorias = [1, 2]  # Bebidas y Snacks
    presupuesto = 30
    articulos = []
    for categoria in categorias:
        articulos += obtener_articulos_por_categoria(categoria)
        
    # 
    
    print("--------------------\n")
    # Verificación de los artículos obtenidos
    #print(f"Artículos obtenidos: {articulos}")
    
    # Convertimos los artículos a una lista de diccionarios
    keys = ["id", "nombre", "precio", "valoracion", "categoria_id", "min", "max"]
    articulos_dict = [dict(zip(keys, articulo)) for articulo in articulos]
    
    print("--------------------\n")
    
    # Verificación de los artículos convertidos a diccionarios
    #print(f"Artículos convertidos a diccionarios: {articulos_dict}")

    # Optimizamos las compras
    resultado = resolver_mochila_limited(articulos_dict, presupuesto)
    # Imprimimos los resultados de manera más atractiva
    print("\nResultado de la optimización:")
    print("Artículos seleccionados:")
    precio_total = 0
    for articulo in resultado['articulos_seleccionados']:
        if articulo['cantidad'] > 0:
            print(f"  - {articulo['nombre']} (Cantidad: {articulo['cantidad']}, Precio: {articulo['precio']}, Valoración: {articulo['valoracion']})")
            precio_total += articulo['cantidad'] * articulo['precio']
    print(f"Valoración total: {resultado['valoracion_total']}")
    print(f"Precio total: {precio_total}")



if __name__ == '__main__':
    main()