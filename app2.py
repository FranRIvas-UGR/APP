# app.py
from database import obtener_articulos_por_categoria, get_categorias
from utils import resolver_mochila_limited_presupuesto
from database import insertar_categoria, insertar_articulo, crear_tablas
import csv, random
import tkinter as tk
from tkinter import messagebox


def leer_csv():
    crear_tablas()
    print("Leyendo datos de productos.csv...")
    categorias = set()
    with open('output_sorted.csv', newline='') as csvfile:
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


def iniciar_interfaz():
            def leer_csv_interfaz():
                leer_csv()
                messagebox.showinfo("Información", "Datos leídos correctamente desde productos.csv")

            def main_interfaz():
                categorias_dict = get_categorias()
                categorias_dict = {k: v for k, v in categorias_dict.items()}

                def seleccionar_categorias():
                    seleccion = entry_categorias.get()
                    selected_ids = [int(id.strip()) for id in seleccion.split(",") if id.strip().isdigit()]
                    if not selected_ids:
                        messagebox.showerror("Error", "Debe seleccionar al menos una categoría.")
                        return
                    categorias = selected_ids
                    articulos = []
                    for categoria in categorias:
                        articulos.append({'categoria_id': categoria, 'articulos_categoria': obtener_articulos_por_categoria(categoria)})

                    keys = ["id", "nombre", "precio", "valoracion", "categoria_id", "min", "max"]
                    articulos_dict = []
                    for articulo in articulos:
                        for item in articulo['articulos_categoria']:
                            if item[0] != 'id':
                                articulos_dict.append(dict(zip(keys, item)))

                    presupuesto = float(entry_presupuesto.get())
                    presupuestos_parciales = {}
                    entry_presupuestos = {}
                    if len(selected_ids) > 1:
                        seRepartePresupuesto = messagebox.askyesno("Repartir presupuesto", "¿Desea repartir el presupuesto entre las categorías?")
                        if seRepartePresupuesto:
                            def fijar_presupuestos():
                                for categoria in categorias:
                                    presupuesto = entry_presupuestos[categoria].get()
                                    presupuestos_parciales[categoria] = float(presupuesto)

                            for categoria in categorias:
                                tk.Label(root, text=f"Ingrese el presupuesto para la categoría {categorias_dict[categoria]}:").pack()
                                entry_presupuestos[categoria] = tk.Entry(root)
                                entry_presupuestos[categoria].pack()
                            tk.Button(root, text="Fijar presupuestos", command=fijar_presupuestos).pack()
                        else:
                            presupuestos_parciales = {categoria: float(presupuesto) / len(categorias) for categoria in categorias}
                    else:
                        presupuestos_parciales = {categorias[0]: presupuesto}
                        
                    entry_num_articulos = {}
                    for categoria in categorias:
                        tk.Label(root, text=f"Ingrese el número de artículos a seleccionar para la categoría {categorias_dict[categoria]}:").pack()
                        entry_num_articulos[categoria] = tk.Entry(root)
                        entry_num_articulos[categoria].pack()
                    
                    def calcular():
                        dic_num_articulos = {}
                        for categoria in categorias:
                            num_articulos = int(entry_num_articulos[categoria].get())
                            dic_num_articulos[categoria] = num_articulos
                        dic_num_articulos = {categoria: int(entry_num_articulos[categoria].get()) for categoria in categorias}
                        for categoria in categorias:
                            resultado_categoria = calcular_productos_categoria(articulos_dict, presupuestos_parciales[categoria], categoria, dic_num_articulos[categoria])
                            crear_ventana_resultados(resultado_categoria)

                    tk.Button(root, text="Calcular", command=calcular).pack()

                root = tk.Tk()
                root.title("Sistema de Recomendación de Compras")
                
                categorias_dict = get_categorias()
                categorias_dict = {k: v for k, v in categorias_dict.items()}
                
                
                def buscar_categoria():
                    query = entry_buscar.get().lower()
                    for widget in frame_categorias.winfo_children():
                        widget.destroy()
                    for id, nombre in categorias_dict.items():
                        if query in nombre.lower():
                            tk.Label(frame_categorias, text=f"{id}: {nombre}").pack()

                tk.Label(root, text="Buscar categoría:").pack()
                entry_buscar = tk.Entry(root)
                entry_buscar.pack()
                tk.Button(root, text="Buscar", command=buscar_categoria).pack()

                frame_categorias = tk.Frame(root)
                frame_categorias.pack()

                tk.Label(root, text="Seleccione las categorías (separadas por comas):").pack()
                entry_categorias = tk.Entry(root)
                entry_categorias.pack()

                tk.Label(root, text="Ingrese el presupuesto:").pack()
                entry_presupuesto = tk.Entry(root)
                entry_presupuesto.pack()
                
                tk.Button(root, text="Seleccionar categorías", command=seleccionar_categorias).pack()

                root.mainloop()

            root = tk.Tk()
            root.title("Sistema de Recomendación de Compras")

            tk.Button(root, text="Leer datos de productos.csv", command=leer_csv_interfaz).pack()
            tk.Button(root, text="Usar la app", command=main_interfaz).pack()

            root.mainloop()
            
def crear_ventana_resultados(resultado):
    root = tk.Tk()
    root.title("Resultados de la optimización")
    
    tk.Label(root, text="Artículos seleccionados:").pack()
    precio_total = 0
    for articulo in resultado['articulos_seleccionados']:
        if articulo['cantidad'] > 0:
            tk.Label(root, text=f"  - {articulo['nombre']} (Cantidad: {articulo['cantidad']}, Precio: {articulo['precio']}, Valoración: {articulo['valoracion']}").pack()
            precio_total += articulo['cantidad'] * articulo['precio']
    tk.Label(root, text=f"Valoración total: {resultado['valoracion_total']}").pack()
    tk.Label(root, text=f"Precio total: {precio_total:.2f}").pack()



if __name__ == '__main__':
    iniciar_interfaz()
        