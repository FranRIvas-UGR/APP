#!/bin/bash

# Borrar el archivo de texto si existe
if [ -f lista_productos.txt ]; then
    rm lista_productos.txt
fi



# Este script ejecuta un programa en PHP y redigire la salida a un archivo de texto

php -f prueba3_csv.php > lista_productos.html